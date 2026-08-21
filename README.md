# 🏥 AI Malnutrition Screening System

A Machine Learning–based web application for screening childhood malnutrition risk using demographic, anthropometric, socioeconomic, and health indicators.

## 📌 Project Overview

The AI Malnutrition Screening System is designed as a public health decision-support tool. It predicts whether a child is likely to be:

* 🔴 **Malnourished**
* 🟢 **Not Malnourished**

The system uses a trained machine learning model and provides prediction probabilities based on child information entered through an interactive Streamlit interface.

## ✨ Features

* 🤖 Machine Learning–based malnutrition prediction
* 👶 Child demographic information
* 📏 Height and weight inputs
* 🦠 Diarrhoea status
* 🎓 Mother's education
* 💰 Household wealth index
* 🏠 Area of residence
* 📊 Prediction probabilities
* 📈 Probability visualization
* 📋 Assessment summary
* 📏 WHO growth data analysis
* 🩺 Stunting, underweight, and wasting indicators
* ⚠️ Public health and clinical disclaimer

## 📊 Input Indicators

The system uses the following indicators:

1. Age
2. Height
3. Weight
4. Sex
5. Diarrhoea in the last two weeks
6. Mother's education
7. Wealth index
8. Area of residence

## 🤖 Machine Learning Model

The model was developed to classify children into two categories:

| Class            | Description                                                            |
| ---------------- | ---------------------------------------------------------------------- |
| Malnourished     | Child identified as potentially at risk of malnutrition                |
| Not Malnourished | Child not classified as malnourished based on the available indicators |

Model evaluation included:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Cross-validation

## 📏 WHO Growth Assessment

The project also incorporates WHO-based anthropometric indicators:

* **HAZ** — Height-for-Age Z-score
* **WAZ** — Weight-for-Age Z-score
* **WHZ** — Weight-for-Height Z-score
* **BAZ** — BMI-for-Age Z-score

These indicators support the analysis of:

* **Stunting**
* **Underweight**
* **Wasting**

## 🗂️ Project Structure

```text
MALNUTRITION_PREDICTION/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── who_combined.csv
│
├── malnutrition_model/
│   ├── malnutrition_model.pkl
│   └── label_encoder.pkl
│
└── venv/
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project folder

```bash
cd MALNUTRITION_PREDICTION
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Running the Application

Run:

```bash
streamlit run app.py
```

The application will open in your web browser.

## ⚠️ Disclaimer

This application is an AI-based screening and decision-support tool. It does **not** replace professional medical, nutritional, or clinical assessment.

Predictions should be interpreted alongside appropriate anthropometric measurements, clinical evaluation, and professional judgment.

## 👩‍💻 Developer

**Joy Kaaria**
BSc Information Technology
Karatina University

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Machine Learning
* WHO Growth Indicators

---

⭐ If you find this project useful, consider giving the repository a star.
