# 👁️ Face Recognition Project

<div align="center">

### 🚀 Real-Time Face Recognition Using Python, OpenCV, InsightFace, and Laptop Camera

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red?style=for-the-badge&logo=opencv)
![InsightFace](https://img.shields.io/badge/InsightFace-Face%20Recognition-green?style=for-the-badge)
![MediaPipe](https://img.shields.io/badge/MediaPipe-AI-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

## 🧠 Detect • Recognize • Identify • Track

A professional real-time face recognition system capable of identifying registered individuals and detecting unknown faces using a laptop webcam.

</div>

---

# 📖 Project Overview

The Face Recognition Project is a real-time computer vision application developed in Python that uses artificial intelligence and deep learning based facial embeddings to recognize people from a local face database.

The system continuously captures video from a laptop camera, detects faces in each frame, extracts facial features, compares them against known identities, and displays recognition results instantly.

##The project currently recognizes:

- 👤 Anees
- 👤 Lubaba
- 👤 Sajid

<img width="1919" height="1080" alt="image" src="https://github.com/user-attachments/assets/ec677514-fcfd-4aab-96f4-694049978276" />



##Any unregistered face is automatically labeled:

❓ Unknown

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/905fa94d-a561-48d9-937e-1c7d1ccbaf4d" />



The project demonstrates practical implementation of:

- Computer Vision
- Artificial Intelligence
- Face Recognition
- Real-Time Video Processing
- Python Software Development
- Deep Learning Applications

---

# 🎯 Problem Statement

Traditional identification systems often depend on physical cards, passwords, fingerprints, or manual verification.

These methods can:

- Be forgotten
- Be stolen
- Be duplicated
- Require physical interaction
- Increase verification time

The objective of this project is to create an intelligent face recognition system capable of automatically identifying authorized individuals directly from a webcam feed while detecting unknown persons in real time.

---

# 🎯 Project Objectives

✅ Detect faces from live webcam feed

✅ Recognize authorized individuals

✅ Label unregistered people as Unknown

✅ Display confidence score

✅ Display FPS (Frames Per Second)

✅ Provide a clean and modular software architecture

✅ Demonstrate practical AI and Computer Vision implementation

✅ Create a scalable foundation for future security applications

---

# 🌟 Key Features

## 👁️ Real-Time Face Detection

Detects faces instantly from live webcam frames.

## 🧠 Face Recognition

Recognizes known people stored inside local folders.

## ❓ Unknown Face Detection

Automatically identifies faces not present in the database.

## 📦 Local Face Database

Uses image folders for training without requiring cloud services.

## ⚡ Fast Processing

Optimized for real-time webcam performance.

## 📊 FPS Monitoring

Displays current frame rate on screen.

## 🔲 Bounding Box Visualization

Highlights detected faces with visual indicators.

## 📛 Identity Labels

Displays recognized person's name.

## 🎯 Confidence Display

Shows confidence value for recognition results.

## 🧩 Modular Architecture

Code separated into professional modules.

## 📈 Easy Scalability

Additional users can be added easily by creating new folders.

---

# 💻 Technologies Used

## Programming Language

- Python 3.12

## Computer Vision Libraries

- OpenCV
- MediaPipe

## Deep Learning Libraries

- InsightFace
- ONNX Runtime

## Scientific Computing

- NumPy

## Development Tools

- VS Code
- Python Virtual Environment
- Windows Operating System

---

# 🏗️ System Architecture

Camera Feed
↓
Frame Capture
↓
Face Detection
↓
Face Alignment
↓
Embedding Extraction
↓
Database Comparison
↓
Identity Matching
↓
Confidence Calculation
↓
Visualization
↓
Output Display

---

# 📂 Project Structure

```text
FaceRecognitionProject/

├── main.py
├── config.py
├── camera.py
├── face_database.py
├── face_detector.py
├── utils.py
├── requirements.txt
├── README.md
├── .gitignore

└── known_faces/

    ├── Anees/
    ├── Lubaba/
    └── Sajid/
```

---

# ⚙️ How the System Works

1. Start Application
2. Load Known Faces
3. Generate Face Embeddings
4. Open Webcam
5. Capture Frames
6. Detect Faces
7. Extract Face Features
8. Compare With Database
9. Calculate Similarity Score
10. Identify Person
11. Display Results
12. Repeat Until Exit

---

# 📷 Dataset Preparation

Create folders:

known_faces/Anees

known_faces/Lubaba

known_faces/Sajid

Add approximately 5 high-quality images for each person.

### Recommended Images

✅ Front Facing

✅ Good Lighting

✅ Clear Face

✅ Multiple Angles

✅ Single Person

### Avoid

❌ Group Photos

❌ Blurry Images

❌ Dark Images

❌ Tiny Faces

❌ Face Coverings

---

# 🧠 Recognition Pipeline

## Step 1: Face Detection

The system first detects faces within the frame.

## Step 2: Face Alignment

Detected faces are aligned to improve recognition accuracy.

## Step 3: Feature Extraction

Unique facial features are extracted.

## Step 4: Embedding Generation

A numerical representation of the face is created.

## Step 5: Similarity Matching

The embedding is compared against stored embeddings.

## Step 6: Identity Decision

Best match is selected.

## Step 7: Confidence Calculation

Recognition confidence is calculated.

## Step 8: Display Results

Bounding box, name, confidence, and FPS are displayed.

---

# 🛠️ Installation Guide

## Create Project Folder

```bash
mkdir FaceRecognitionProject
cd FaceRecognitionProject
```

## Create Virtual Environment

```bash
py -3.12 -m venv venv
```

## Activate Environment

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install opencv-python numpy insightface onnxruntime mediapipe
```

## Save Requirements

```bash
pip freeze > requirements.txt
```

---

# ▶️ Running the Project

```bash
python main.py
```

or

```bash
py -3.12 main.py
```

---

# 🖼️ Project Demonstration

## 👤 Known Person Recognition

Add your screenshot here:

```md
![Recognized Face](images/recognized-face.jpg)
```

The system successfully:

- Detects face
- Recognizes person
- Displays name
- Displays confidence
- Draws bounding box

---

## ❓ Unknown Face Detection

Add your screenshot here:

```md
![Unknown Face](images/unknown-face.jpg)
```

The system successfully:

- Detects face
- Fails safe when identity is unknown
- Labels face as Unknown
- Prevents incorrect recognition

---

# 📊 Expected Output

When running successfully:

✅ Live webcam feed

✅ Face detection

✅ Face recognition

✅ Unknown face detection

✅ Confidence score

✅ FPS display

✅ Real-time updates

---

# 🧪 Testing Methodology

## Test 1

Camera initialization

## Test 2

Single user recognition

## Test 3

Multiple user recognition

## Test 4

Unknown face detection

## Test 5

Different lighting conditions

## Test 6

Different camera distances

## Test 7

Different viewing angles

## Test 8

Long-duration operation

---

# 📈 Performance Evaluation

| Feature | Result |
|----------|----------|
| Face Detection | Successful |
| Face Recognition | Successful |
| Unknown Detection | Successful |
| Real-Time Processing | Successful |
| Multiple Tests | Stable |
| FPS Monitoring | Working |

---

# ⚠️ Challenges Faced

- Dataset quality management
- Lighting variation handling
- Recognition threshold tuning
- Webcam performance optimization
- Unknown face classification
- Dependency compatibility

---

# 🚀 Future Enhancements

## Smart Attendance System

- Attendance logging
- Daily reports
- Excel export

## Security System

- Access control
- Door unlocking
- User authentication

## AI Improvements

- Emotion recognition
- Age estimation
- Gender detection
- Face tracking

## Cloud Integration

- Database storage
- Remote monitoring
- Web dashboard

## Advanced Security

- Liveness detection
- Anti-spoofing
- Multi-factor authentication

---

# 🎓 Learning Outcomes

Through this project, practical experience was gained in:

- Python Development
- OpenCV
- MediaPipe
- InsightFace
- ONNX Runtime
- Computer Vision
- Artificial Intelligence
- Real-Time Systems
- Software Architecture
- Dataset Management
- Performance Optimization

---

# 💼 Applications

- Smart Attendance Systems
- Access Control Systems
- Security Monitoring
- Smart Offices
- Smart Homes
- Visitor Management
- AI Surveillance Systems
- Research and Education

---

# 🌍 Real World Impact

Face recognition technology is increasingly used in:

- Airports
- Smart Cities
- Banking Systems
- Educational Institutions
- Industrial Security
- Enterprise Authentication

This project serves as a practical demonstration of those technologies at a smaller scale.

---

# 💡 Why This Project Matters

This project combines:

- Artificial Intelligence
- Deep Learning
- Computer Vision
- Real-Time Processing
- Software Engineering

into a single practical solution.

It demonstrates both theoretical understanding and practical implementation skills.

---

# ✅ Conclusion

The Face Recognition Project successfully demonstrates the implementation of a real-time facial recognition system using Python and modern computer vision technologies.

The system can identify authorized individuals, detect unknown faces, display confidence scores, and operate in real time through a laptop webcam.

The modular design allows future expansion into advanced security, attendance, and smart automation applications.

---

# 👨‍💻 Author

## Anees Ur Rehman

📧 Email: eng.aneesrehman@gmail.com

📱 Contact No.: +92 333 6129332

---

# 📜 License

This project is intended for educational, research, and portfolio purposes.
