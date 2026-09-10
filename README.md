# ☁️ Predictive Cloud Resource Auto-Scaling using Machine Learning

A machine learning-based cloud resource prediction system that forecasts CPU utilization and recommends auto-scaling decisions (Scale Up, Keep Current Resources, or Scale Down). The project uses the Google 2019 Cluster Sample dataset and compares multiple regression models to optimize cloud resource allocation.

## 📌 Project Overview

Cloud applications experience fluctuating workloads throughout the day. Traditional rule-based auto-scaling reacts only after resource utilization crosses predefined thresholds, which may lead to delayed scaling and inefficient resource usage.

This project predicts future CPU utilization using machine learning and provides intelligent scaling recommendations to improve resource efficiency.

## 🚀 Features

* Exploratory Data Analysis (EDA) of cloud workload data
* Data preprocessing and feature engineering
* Comparison of three ML models:

  * Linear Regression
  * Random Forest Regressor
  * Gradient Boosting Regressor
* Performance evaluation using MAE, RMSE, and R² Score
* Streamlit web application for real-time prediction
* Automatic scaling recommendation based on predicted CPU utilization

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** Pandas, NumPy, Matplotlib, Scikit-learn, Joblib
* **Frontend:** Streamlit
* **Dataset:** Google 2019 Cluster Sample (Kaggle)

## 📂 Project Structure

```text
cloud-scaler-ml/
│
├── data/
│   ├── cleaned_cluster_data.csv
│   ├── X.csv
│   └── y.csv
│
├── notebooks/
│   └── EDA.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── train_model.py
│   └── predict.py
│
├── models/
├── app.py
├── requirements.txt
└── README.md
```

## 📊 Machine Learning Results

| Model             | R² Score   | RMSE         |
| ----------------- | ---------- | ------------ |
| Linear Regression | **0.8662** | 0.006851     |
| Random Forest     | **0.9995** | **0.000399** |
| Gradient Boosting | **0.9625** | 0.003628     |

**Best Model:** Random Forest Regressor

## ⚙️ Auto-Scaling Logic

| Predicted CPU | Recommendation            |
| ------------- | ------------------------- |
| Below 40%     | 🟢 Scale Down             |
| 40% – 75%     | 🟡 Keep Current Resources |
| Above 75%     | 🔴 Scale Up               |

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/sampatil232/cloud-scaler-ml.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Train the model

```bash
cd src
python train_model.py
```

4. Launch the Streamlit app

```bash
cd ..
streamlit run app.py
```

## 📈 Future Improvements

* Time-series forecasting using LSTM
* Real-time cloud monitoring dashboard
* Kubernetes integration for automatic scaling
* AWS/GCP deployment

## 👩‍💻 Author

**Samiksha Patil**

B.Tech Computer Science & Engineering (Cybersecurity)

D Y Patil International University
