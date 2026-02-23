# 👷 Safety Helmet Detection System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Framework](https://img.shields.io/badge/Framework-Flask-green)
![AI Model](https://img.shields.io/badge/AI-YOLOv8-orange)
![Cloud](https://img.shields.io/badge/Cloud-Azure_Blob_Storage-0078D4)

## 📌 Project Overview
This project is an automated safety monitoring system designed to ensure construction or factory workers are wearing proper safety headgear. 

Using a **YOLOv8** deep learning model and **OpenCV**, the system analyzes a live video feed in real-time. If it detects a person without a helmet, it automatically captures the frame, highlights the violation with bounding boxes, and uploads the evidence instantly to **Microsoft Azure Blob Storage** for record-keeping.

## 🚀 Key Features
* **Real-Time Detection:** Processes video frames instantly to identify "Person" and "Helmet" classes.
* **Smart Violation Logic:** Triggers an alert only if the number of people exceeds the number of helmets detected.
* **Cloud Integration:** Automatically pushes violation images to an Azure Blob Storage container.
* **Performance Optimized:** Uses Python threading to upload images in the background without freezing the live video feed.
* **Spam Prevention:** Includes a cooldown timer (15 seconds) to prevent duplicate uploads of the same incident.

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **Computer Vision:** OpenCV (`cv2`), Ultralytics YOLO (`v8`)
* **Cloud Storage:** Azure Blob Storage SDK
* **Environment Management:** `python-dotenv`

## ⚙️ Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/your-username/safety-helmet-detection.git](https://github.com/your-username/safety-helmet-detection.git)
    cd safety-helmet-detection
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Secrets**
    Create a `.env` file in the root directory and add your Azure credentials:
    ```ini
    AZURE_API_KEY="your_actual_azure_connection_string_here"
    ```
    *(Note: The connection string typically looks like `DefaultEndpointsProtocol=https;AccountName=...`)*

4.  **Run the Application**
    ```bash
    python app.py
    ```

## 📂 Project Structure
