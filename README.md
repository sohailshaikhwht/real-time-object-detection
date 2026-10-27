# Real-Time Object Detection using YOLO and OpenCV

## 📌 Project Overview

This project implements a Real-Time Object Detection System using Python, OpenCV, and YOLO26n.

The system uses a webcam to capture live video frames and applies a pretrained YOLO model to identify and detect multiple objects in real time.

It displays bounding boxes, object labels, confidence-based detections, FPS (Frames Per Second), and the total number of detected objects.

## 🚀 Features

* Real-time object detection using a webcam.
* YOLO26n pretrained deep learning model.
* Object identification with bounding boxes and labels.
* Confidence threshold-based detection.
* Live FPS (Frames Per Second) calculation.
* Total number of detected objects.
* Class-wise object counting.
* Live video processing using OpenCV.
* Lightweight model for efficient inference.

## 🛠️ Technologies Used

| Technology  | Purpose                                           |
| ----------- | ------------------------------------------------- |
| Python      | Core programming language                         |
| YOLO26n     | Object detection model                            |
| OpenCV      | Webcam access and image processing                |
| Ultralytics | YOLO model integration                            |
| NumPy       | Numerical operations used by the vision libraries |

## 📂 Project Structure

```text
real-time-object-detection/
│
├── main.py          # Main object detection program
├── yolo26n.pt       # Pretrained YOLO model
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sohailshaikhwht/real-time-object-detection.git
```

### 2. Navigate to the Project Folder

```bash
cd real-time-object-detection
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Virtual Environment (Windows)

```bash
.venv\Scripts\activate
```

### 5. Install Required Libraries

```bash
pip install ultralytics opencv-python
```

## ▶️ How to Run

Execute the following command:

```bash
python main.py
```

The webcam will start automatically, and the system will begin detecting objects in real time.

**To exit the application:** Press `Q` on your keyboard.

## 🧠 How It Works

1. **Model Loading:** Loads the pretrained YOLO26n model.
2. **Video Capture:** OpenCV accesses the system webcam.
3. **Frame Processing:** Captures and processes video frames continuously.
4. **Object Detection:** YOLO identifies objects in each frame.
5. **Visualization:** Draws bounding boxes and object labels.
6. **Object Counting:** Calculates the total number of detected objects and counts objects by class.
7. **Performance Monitoring:** Calculates and displays real-time FPS.

## 📊 Output

The application displays:

* Detected object names.
* Bounding boxes around detected objects.
* Total detected objects.
* Object counts by category.
* Real-time FPS performance.

## 🎯 Applications

* Smart surveillance systems.
* Traffic monitoring.
* Retail object detection.
* Industrial automation.
* Security monitoring.
* Computer vision applications.
* AI-powered monitoring systems.

## 🔮 Future Improvements

* Add image and video file detection.
* Implement object tracking.
* Add object counting and analytics dashboard.
* Support custom-trained YOLO models.
* Improve detection performance using GPU acceleration.
* Develop a web-based interface.

## 👨‍💻 Author

**Sohail Shaikh**

GitHub: https://github.com/sohailshaikhwht

## ⭐ Support

If you find this project useful, consider giving it a star on GitHub!

---

**Built with Python, OpenCV, and YOLO for Real-Time Computer Vision.**
