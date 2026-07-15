# 🌿 AI Plant Disease Detection System

An end-to-end **Deep Learning-based Plant Disease Detection System** built using **TensorFlow, EfficientNet-B0, and Streamlit**. The application identifies plant diseases from leaf images, provides detailed disease information, recommends treatment and preventive measures, and generates a professional PDF report.

## 🚀 Live Demo

**Application:** https://ai-plant-disease-detection-system-aia2mf3uskfaojtfuoyvhk.streamlit.app/

## 📂 GitHub Repository

**Repository:** https://github.com/PratikNagdeve/AI-Plant-Disease-Detection-System

---

# 📌 Project Overview

Plant diseases are a major cause of agricultural yield loss worldwide. Early detection enables farmers and agricultural professionals to take timely corrective actions, reducing crop damage and improving productivity.

This project utilizes **Transfer Learning with EfficientNet-B0** to classify plant leaf diseases across **15 different classes** from the PlantVillage dataset. The trained model is deployed as a user-friendly Streamlit web application that allows users to upload leaf images, receive disease predictions, explore treatment recommendations, and download a detailed PDF report.

---

# ✨ Features

* 🌱 Plant disease detection from uploaded leaf images
* 🤖 EfficientNet-B0 transfer learning model
* 📊 **94.21% Test Accuracy**
* 📖 Built-in disease knowledge base
* 💊 Treatment recommendations
* 🛡 Preventive measures
* 📄 Professional PDF report generation
* 🌐 Interactive Streamlit web application
* 📱 Clean and responsive user interface

---

# 🌿 Supported Plant Diseases

The system supports prediction of the following **15 classes**:

| Crop        | Disease                       |
| ----------- | ----------------------------- |
| Bell Pepper | Bacterial Spot                |
| Bell Pepper | Healthy                       |
| Potato      | Early Blight                  |
| Potato      | Late Blight                   |
| Potato      | Healthy                       |
| Tomato      | Bacterial Spot                |
| Tomato      | Early Blight                  |
| Tomato      | Late Blight                   |
| Tomato      | Leaf Mold                     |
| Tomato      | Septoria Leaf Spot            |
| Tomato      | Spider Mites                  |
| Tomato      | Target Spot                   |
| Tomato      | Tomato Yellow Leaf Curl Virus |
| Tomato      | Tomato Mosaic Virus           |
| Tomato      | Healthy                       |

---

# 🧠 Model Architecture

The application uses **Transfer Learning** with **EfficientNet-B0**.

Architecture:

* EfficientNet-B0 (ImageNet Pretrained)
* Global Average Pooling Layer
* Dense Layer (256 Units)
* Dropout Layer
* Softmax Classification Layer

---

# 📊 Model Performance

| Metric            | Value              |
| ----------------- | ------------------ |
| Test Accuracy     | **94.21%**         |
| Number of Classes | **15**             |
| Image Size        | **224 × 224**      |
| Batch Size        | **32**             |
| Framework         | TensorFlow / Keras |

---

# 📂 Project Structure

```text
AI-Plant-Disease-Detection-System/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── sample_images/
│
├── models/
│   ├── best_model.keras
│   └── plant_disease_model.py
│
├── scripts/
│   ├── download_dataset.py
│   ├── explore_dataset.py
│   ├── visualize_dataset.py
│   ├── preprocessing.py
│   ├── data_pipeline.py
│   ├── train.py
│   ├── evaluate_model.py
│   ├── predict.py
│   └── test_pdf.py
│
├── utils/
│   ├── disease_info.py
│   ├── predictor.py
│   └── pdf_generator.py
│
└── reports/
```

---

# 🛠 Technology Stack

* Python
* TensorFlow
* Keras
* EfficientNet-B0
* Streamlit
* NumPy
* Pillow
* Scikit-learn
* ReportLab

---

# 📚 Dataset

This project uses a subset of the **PlantVillage Dataset**, one of the most widely used benchmark datasets for plant disease classification. The original PlantVillage dataset contains over 54,000 labeled images spanning multiple crop species and diseases.

The dataset is **not included** in this repository due to its large size.

---

# 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/PratikNagdeve/AI-Plant-Disease-Detection-System.git
cd AI-Plant-Disease-Detection-System
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

# 💻 Usage

1. Upload a plant leaf image.
2. Click **Detect Disease**.
3. View the predicted crop and disease.
4. Review the confidence score.
5. Read the disease description.
6. Explore possible causes.
7. View treatment recommendations.
8. Learn preventive measures.
9. Download the generated PDF report.

---

# 📄 PDF Report

The application generates a downloadable PDF report containing:

* Uploaded leaf image
* Date and time of analysis
* Crop name
* Disease prediction
* Confidence score
* Disease description
* Possible causes
* Treatment recommendations
* Preventive measures

---

# 🔮 Future Improvements

* Support for additional crop species
* Multi-language interface
* Grad-CAM explainable AI visualization
* Disease severity estimation
* Fertilizer recommendation system
* Weather-based disease alerts
* Mobile application support
* Cloud database integration

---

# 👨‍💻 Developer

**Pratik Nagdeve**

M.Tech in Artificial Intelligence

Maulana Azad National Institute of Technology (MANIT), Bhopal

---

# 📜 License

This project is intended for educational and research purposes.

---

# ⭐ Support

If you found this project useful, consider giving the repository a **Star ⭐** on GitHub.
