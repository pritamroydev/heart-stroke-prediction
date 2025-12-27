# 🧠 Heart Stroke Prediction System

A Machine Learning–based web application that predicts the risk of heart stroke using clinical and lifestyle parameters.  
The project covers the **complete ML pipeline** — from data preprocessing and model training to deployment using **Streamlit Cloud**.

---

## 🚀 Live Demo
🔗 https://<heart-stroke-prediction>.streamlit.app  
*(Replace with your actual Streamlit Cloud link after deployment)*

---

## 📌 Project Overview

Heart stroke is a critical medical condition that requires early risk assessment.  
This project aims to assist in identifying individuals at **low, moderate, or high risk of stroke** using supervised machine learning models.

The system:
- Accepts user health inputs
- Applies the same preprocessing used during training
- Predicts stroke risk using trained ML models
- Displays results via an interactive Streamlit interface

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Libraries:**  
  - NumPy  
  - Pandas  
  - Scikit-learn  
  - Joblib  
  - Streamlit  
  - Matplotlib / Seaborn  
- **Deployment:** Streamlit Cloud  
- **Version Control:** Git & GitHub  

---

## 🧩 Machine Learning Models Used

The following models were trained and evaluated:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- Support Vector Classifier (SVC)

Each model was saved using `joblib` for inference during deployment.

---

## 🔄 Workflow

1. Dataset collection (Kaggle)
2. Data cleaning and preprocessing
3. Feature encoding and scaling
4. Train–test split
5. Model training and evaluation
6. Model and scaler persistence (`.pkl`)
7. Streamlit frontend integration
8. Deployment on Streamlit Cloud

---

## 📂 Project Structure
heart-stroke-prediction/
│
├── app.py
│   └── Streamlit web application for heart stroke prediction
│
├── models/
│   ├── scaler.pkl
│   ├── stroke_logistic_model.pkl
│   ├── stroke_knn_model.pkl
│   ├── stroke_svc_model.pkl
│   ├── stroke_decision_tree_model.pkl
│   └── stroke_random_forest_model.pkl
│
├── notebook/
│   └── Heart_Stroke_Prediction_Final.ipynb
│       └── Contains data cleaning, EDA, feature engineering,
│           model training, evaluation, and model saving
│
├── docs/
│   ├── Project_Report.pdf
│   └── Project_Presentation.pptx
│
├── requirements.txt
│   └── Python dependencies required to run the Streamlit app
│
├── README.md
│   └── Project overview, setup instructions, and team details
│
├── .gitignore
│   └── Git ignore rules (virtual environment, cache files, datasets)


## 👥 Team Members

- **Pritam Roy** — Project Lead, ML Model Development, Presentation, Documentation, Deployment
- **Supritam Mukhopathay** — Frontend Design, UI Feedback, Documentation
- **Rhitinkar Bhowmik** — Data Preprocessing, Presentation, Documentation
- **Srikanta Maji** — Data Visualization, Documentation

