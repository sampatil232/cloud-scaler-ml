import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/random_forest.pkl")

st.set_page_config(page_title="Cloud Auto-Scaler", layout="centered")

st.title("☁️ Predictive Cloud Resource Auto-Scaling")

st.write("Enter the current cloud resource values to predict CPU utilization.")

# User Inputs
avg_memory = st.slider("Average Memory Usage", 0.0, 1.0, 0.05, 0.01)
max_cpu = st.slider("Maximum CPU Usage", 0.0, 1.0, 0.10, 0.01)
max_memory = st.slider("Maximum Memory Usage", 0.0, 1.0, 0.08, 0.01)
assigned_memory = st.slider("Assigned Memory", 0.0, 1.0, 0.10, 0.01)
failed = st.selectbox("Task Failed", [0, 1])

if st.button("Predict CPU Utilization"):

    sample = pd.DataFrame({
        "avg_memory": [avg_memory],
        "max_cpu": [max_cpu],
        "max_memory": [max_memory],
        "assigned_memory": [assigned_memory],
        "failed": [failed]
    })

    prediction = model.predict(sample)[0]
    cpu_percent = prediction * 100

    st.metric("Predicted CPU Utilization", f"{cpu_percent:.2f}%")

    if cpu_percent > 75:
        st.error("Scale Up: Add more virtual machines")
    elif cpu_percent < 40:
        st.success("Scale Down: Reduce unused resources")
    else:
        st.info("Keep Current Resources")