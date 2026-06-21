# SmartScale-AI
ML-powered traffic forecasting and infrastructure scaling dashboard

# 🚀 SmartScale AI

ML-powered traffic forecasting and infrastructure scaling dashboard built with Python, Machine Learning, and Streamlit.

## 📌 Overview

SmartScale AI predicts future website traffic, estimates infrastructure requirements, identifies operational risks, and generates executive PDF reports for decision-making.

The system uses a Multiple Linear Regression model trained on website traffic patterns including weekends, holidays, sales campaigns, and seasonal effects.

---

## ✨ Features

### 📈 Traffic Forecasting

* Predict future website traffic
* Multiple business scenarios
* AI-powered demand estimation

### 🖥 Infrastructure Planning

* Automatic server requirement calculation
* Capacity sufficiency analysis
* Additional server recommendations

### ⚠ Risk Assessment

* LOW risk
* MEDIUM risk
* HIGH risk
* CRITICAL risk

### 📊 Business Insights

* Weekend traffic analysis
* Sales campaign impact analysis
* Historical traffic visualization

### 📄 PDF Executive Reports

* Prediction summary
* Infrastructure status
* Cost estimation
* Peak traffic analysis
* Business recommendations

### 🔮 7-Day Forecast

* Future traffic forecasting
* Peak traffic day detection
* Trend visualization

---

## 🛠 Tech Stack

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-Learn
* ReportLab
* Git & GitHub

---

## 📂 Project Structure

SmartScale-AI/

├── app/

│ └── app.py

├── data/

│ └── traffic_data.csv

├── src/

│ ├── generate_data.py

│ ├── load_data.py

│ ├── predictor.py

│ ├── report_generator.py

│ └── train_model.py

└── README.md

---

## 🚀 How To Run

### Clone Repository

```bash
git clone https://github.com/elevenyush/SmartScale-AI.git
cd SmartScale-AI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app/app.py
```

---

## 📊 Machine Learning Model

Model Used:

* Multiple Linear Regression

Features:

* Month
* Day of Week
* Weekend Indicator
* Holiday Indicator
* Sale Campaign Indicator

Dataset Size:

* 365 Days

---

## 🎯 Future Improvements

* Random Forest Regression
* XGBoost Forecasting
* Real-Time Traffic API Integration
* Cloud Deployment
* Auto-Scaling Recommendations
* Interactive Business Analytics Dashboard

---

## 👨‍💻 Author

Ayushman Gupta

Built as a Machine Learning + Operations Analytics project demonstrating forecasting, infrastructure planning, and business intelligence using Python and Streamlit.
