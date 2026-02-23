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
├── app.py              # Main Flask application and logic
├── best.pt             # Trained YOLOv8 model weights
├── requirements.txt    # List of python dependencies
├── .env                # (Excluded) Stores Azure secrets
└── templates/
└── index.html      # Frontend for video strea

Gemini said
Here is the professional content you can copy and paste directly into your GitHub repository.

1. GitHub "About" Section (The Right Sidebar)
Description:

A real-time AI computer vision system that detects safety helmet violations and automatically logs evidence to the cloud. Built with Python, Flask, YOLOv8, and Azure Blob Storage.

Topics (Tags):

computer-vision yolov8 flask azure-blob-storage python artificial-intelligence safety-detection opencv

2. The README.md File
Create a file named README.md and paste this entire block of code inside.

Markdown
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
├── app.py              # Main Flask application and logic
├── best.pt             # Trained YOLOv8 model weights
├── requirements.txt    # List of python dependencies
├── .env                # (Excluded) Stores Azure secrets
└── templates/
└── index.html      # Frontend for video stream


## 🔮 Future Scope
* **Email Alerts:** Send an immediate email notification to the supervisor when a violation occurs.
* **Dashboard:** Build a frontend admin panel to view the history of uploaded violation images from Azure.
* **Edge Deployment:** Optimize the model to run on edge devices like a Raspberry Pi or NVIDIA Jetson Nano.

## 🤝 Contributing
Contributions are welcome! Please fork the repository and create a pull request.

---
*Developed by Amit Kushwaha | Silver Oak University*


