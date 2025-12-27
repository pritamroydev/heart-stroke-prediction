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

