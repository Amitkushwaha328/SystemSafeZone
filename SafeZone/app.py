from flask import Flask, render_template, request, jsonify
from ultralytics import YOLO
import cv2
import numpy as np
import base64
import threading
import time
from datetime import datetime
from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv

app = Flask(__name__)
# This automatically loads the secrets from your .env file
load_dotenv()

# 1. Grab the connection string safely from the .env file
AZURE_CONNECTION_STRING = os.getenv("AZURE_API_KEY")

# 2. Define your Azure Blob Storage container name here
# (Make sure you have created a container with this exact name in the Azure Portal)
CONTAINER_NAME = "violations" 

# --- BACKGROUND UPLOAD FUNCTION ---
def upload_to_azure(image_bytes, blob_name):
    try:
        # Check if the connection string loaded properly
        if not AZURE_CONNECTION_STRING:
            print("❌ ERROR: Azure Connection String is missing. Check your .env file.")
            return

        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)
        
        # Upload the raw image bytes directly to the cloud
        blob_client.upload_blob(image_bytes, overwrite=True)
        print(f"☁️ SUCCESS: Uploaded {blob_name} to Azure!")
    except Exception as e:
        print(f"❌ AZURE ERROR: {e}")

# --- AI & SERVER SETUP ---
print("Loading AI Model...")
model = YOLO('best.pt')
print("Model Loaded. Server Ready.")

# Timer to prevent spamming Azure with 100 uploads a minute
last_upload_time = 0
UPLOAD_COOLDOWN = 15  # Wait 15 seconds before uploading another violation

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/verify_access', methods=['POST'])
def verify_access():
    global last_upload_time
    
    # 1. Get and Decode the Image
    data = request.json
    image_data = data['image']
    encoded_data = image_data.split(',')[1]
    
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # 2. Run the AI
    results = model(frame, verbose=False)
    
    person_count = 0
    helmet_count = 0

    for r in results:
        for box in r.boxes:
            conf = float(box.conf[0])
            if conf > 0.50:
                cls = int(box.cls[0])
                label = model.names[cls].lower()
                
                if "person" in label: 
                    person_count += 1
                if ("helmet" in label or "hardhat" in label) and "no" not in label: 
                    helmet_count += 1

    # 3. Access Logic & Azure Trigger
    current_time = time.time()

    if person_count == 0:
        return jsonify({"status": "WAITING", "message": "No person detected"})
    
    elif person_count > helmet_count:
        # VIOLATION DETECTED!
        if (current_time - last_upload_time) > UPLOAD_COOLDOWN:
            # We draw the AI bounding boxes on the frame so the Azure proof looks professional
            annotated_frame = results[0].plot()
            
            # Convert the frame back to bytes for uploading
            _, buffer = cv2.imencode('.jpg', annotated_frame)
            annotated_bytes = buffer.tobytes()
            
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            blob_name = f"violation_{timestamp}.jpg"
            
            # Send to Azure in the background!
            threading.Thread(target=upload_to_azure, args=(annotated_bytes, blob_name)).start()
            
            last_upload_time = current_time

        return jsonify({"status": "DENIED", "message": "Helmet missing"})
        
    else:
        # Fully Equipped
        return jsonify({"status": "GRANTED", "message": "Safe"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)