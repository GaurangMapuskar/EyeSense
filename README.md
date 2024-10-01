
# EyeSense

## Project Overview
EyeSense is an AI-powered web application developed to assist visually impaired individuals, providing real-time auditory feedback to help them navigate their surroundings and inquire about product prices. The application uses advanced object detection technology, specifically the YOLO algorithm, to offer greater independence and accessibility to users.

## Key Features
- **Real-time Object Detection**: Utilizes YOLO (You Only Look Once) technology to detect and provide auditory descriptions of objects in the environment.
- **Product Price Inquiry**: Helps users inquire about prices of products in stores for a seamless shopping experience.
- **User-Friendly Interface**: Designed with simplicity and ease-of-use in mind, featuring customizable settings to meet individual user preferences.
- **Data Privacy and Security**: Ensures user data is secure, with strong encryption and compliance with privacy regulations.

## Dataset
For the currency detection feature, we have used the following dataset:
- [Indian Currency Notes Dataset for YOLOv5](https://www.kaggle.com/datasets/gowthamreddyuppunuri/indian-currency-notes-used-for-yolov5)

## Technology Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python Framework)
- **Object Detection**: YOLOv8 (You Only Look Once)
- **Image Processing**: OpenCV
- **Speech Processing**: Text-to-Speech technologies

## Installation Guide
1. Clone the repository:
   ```bash
   git clone https://github.com/GaurangMapuskar/EyeSense.git
   ```
2. Navigate to the project directory:
   ```bash
   cd EyeSense
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Access the application via your browser at `http://127.0.0.1:5000/`

## Project Structure
```
EyeSense/
│
├── __pycache__/                 # Python cache files
│
├── functions/                   # Core functions for detection and training
│   ├── Currency.pt              # Pretrained model for currency detection
│   ├── Trainer.yml              # Training configuration file
│   ├── best.pt                  # Best weights for object detection
│   ├── currency_detection.py    # Currency detection logic
│   ├── datacollect.py           # Data collection logic
│   ├── face_detection.py        # Face detection logic
│   ├── haarcascade_frontalface_default.xml  # Haar cascade for face detection
│   ├── object_description.py    # Describing detected objects
│   ├── object_detection.py      # Object detection logic
│   └── trainingdemo.py          # Demo for training models
│
├── img/                         # Images used in the project
│   ├── currency_recognition.png
│   ├── face_recognition.png
│   ├── logo.png
│   ├── object_detect.jpg
│   ├── object_detection.png
│   └── t2s.png
│
├── templates/                   # HTML templates for the web app
│   ├── about.html               # About page
│   ├── contact.html             # Contact page
│   ├── currency.html            # Currency detection interface
│   ├── description.html         # Object description interface
│   ├── face.html                # Face recognition interface
│   ├── index.html               # Main homepage
│   ├── object.html              # Object detection interface
│   └── styles.css               # Stylesheets
│
├── LICENSE                      # License file
├── app.py                       # Main Flask application file
├── camera.py                    # Camera module for capturing images
├── captured_image.jpg           # Last captured image
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

## System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Hardware**:
  - Dual-core processor
  - 4GB RAM
  - 128GB SSD storage
  - Web Camera for object detection
- **Software**:
  - Python 3.x
  - Flask Framework
  - OpenCV
  - YOLOv8 Model

## Usage
Once the application is running, visually impaired users can:
- Use their device's camera to detect nearby objects.
- Receive auditory feedback describing detected objects.
- Inquire about product prices by pointing the camera towards store items.

## Future Scope
- Expand to mobile platforms (iOS, Android).
- Integrate with smart assistive devices (e.g., smart canes).
- Enhance object recognition accuracy.
- Collaborate with accessibility organizations for continuous improvement.

## Authors
- Ameya Angne
- Mitesh Dalvi
- Anushka Karhadkar
- Gaurang Mapuskar

## License
This project is licensed under the [MIT License](LICENSE).
