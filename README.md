# 🗑️ AI-Powered Smart Waste Management Dashboard

**A prototype platform that combines deep learning and IoT-inspired features for real-time waste classification and smart bin monitoring.**

Built for sustainability and civic automation projects, this dashboard demonstrates how modern AI and data tools can advance waste management in communities and institutions.

---

## 📋 Project Overview

Modern cities face growing challenges in sustainable waste disposal—sorting recyclable materials, avoiding overfilled bins, and reducing manual work.

This project demonstrates a full-stack machine learning prototype for **waste classification** and **smart bin status tracking**, combining image classification (deep learning) with an interactive web dashboard built with Streamlit.

## 🚀 Features

* **AI Waste Classifier:** Instantly categorize uploaded images of waste as **Plastic**, **Paper**, or **Metal** using a CNN-based AI model.
* **Smart Bin Monitoring (Simulation):** Track real-time simulated fill levels for multiple bins. Alerts are displayed when bins approach capacity, showcasing the system’s IoT-readiness.
* **Intuitive Streamlit Dashboard:** Web-based, mobile-friendly interface for admins/operators to quickly classify waste and monitor bins.
* **Real-World Ready:** Code design allows easy extension to true IoT integration (e.g., directly connecting with sensor APIs/devices).

---

## 📁 Project Structure

```text
smart_waste_management/
│
├── ai_model/
│   ├── train_model.py          # Image classifier training script
│   ├── utils.py                # (Optional) Preprocessing/augmentation utilities
│   └── waste_classifier_model.h5 # Trained Keras/TensorFlow model
│
├── dashboard/
│   └── app.py                  # Streamlit dashboard application
│
├── data/
│   └── train/
│       ├── Plastic/
│       ├── Paper/
│       └── Metal/              # Training images sorted by class
│
│   
│
└── README.md
```
---

## 🧠 Model & Data

### Model:
Keras/TensorFlow CNN (e.g., MobileNetV2 or custom): designed to generalize well even with limited training samples.

### Classes:
Plastic, Paper, Metal (can be expanded to more types as needed).

### Training Data:
Images are organized by class in data/train/. For best results, use ≥30 images per class.
(Open/public image datasets or your own labeled photos can be used.)

---

## 🛠️ Installation & Environment Setup

1. Clone the repository:

```text
bash
git clone https://github.com/yourusername/smart_waste_management.git
cd smart_waste_management
```

2. Create & activate a Python 3.10 virtual environment:

```text
bash
python3.10 -m venv smart_waste_venv
source smart_waste_venv/bin/activate
pip install --upgrade pip
```

3. Install required packages:

```text
bash
pip install tensorflow-macos tensorflow-metal streamlit numpy Pillow
```

Note: For Apple Silicon (M1/M2/M3), TensorFlow-macos and TensorFlow-metal are required for GPU acceleration.

---

## 🏋️‍♂️ Training the Model
Place images for each class (Plastic, Paper, Metal) inside respective subfolders in data/train/.

Run:

```text
bash
python ai_model/train_model.py
```

Trained model will be saved as ai_model/waste_classifier_model.h5 (legacy HDF5 format for demo).

---

## 🌍 Running the Dashboard
Start the Streamlit dashboard by running:

```text
bash
streamlit run dashboard/app.py
```

Access the dashboard at http://localhost:8501 in your browser.

---

## 📖 Usage Guide

* Upload a Waste Image:
  Use the uploader to select or drag-and-drop a waste image.

* Get Prediction:
  The dashboard displays the predicted category and confidence score.

* Monitor Bins:
  See the percentage fill and automatic alerts for "Bin A", "Bin B", and "Bin C" (dummy data is used for now).

---

## 📝 Customization & Roadmap

* Expand Classes: Add more waste types for classification.

* Advanced UI: Add charts, data history, or analytics.

* IoT Integration: Connect to actual bin sensors for real-time monitoring.

* Deployment: Host dashboard on cloud/server for continuous access.

* Enhancements: Add user authentication, notifications, and scheduling.

---

## 🔧 Troubleshooting
* Blank Dashboard: Add print/logging or check app.py error handling for file/model issues.

* Model Not Loading: Confirm waste_classifier_model.h5 path and compatible Keras/TensorFlow versions.

* Slow Performance: Upgrade hardware or optimize image/model size.

---

## 🤝 Contributing
* Have an idea, feature, or improvement?
* Open an issue, create a PR, or fork and experiment!
* Contributions, bug reports, and suggestions are all welcome.

---

## 📜 License
MIT License. See LICENSE for details.

---

## 📣 Acknowledgements
TensorFlow and Keras

Streamlit

NumPy

Open-source datasets and developers who inspire sustainable ML projects
