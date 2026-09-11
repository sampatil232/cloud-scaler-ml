import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/random_forest.pkl")

st.set_page_config(page_title="Cloud Auto-Scaler", layout="centered")

st.title("☁️ Predictive Cloud Resource Auto-Scaling")

st.write("Enter the current cloud resource values to predict CPU utilization.")

st.markdown("### Resource Usage Reference")

st.table(pd.DataFrame({
    "Workload": ["🟢 Low / Idle", "🟡 Normal", "🔴 High / Peak"],
    "Suggested Values": [
        "10–30% CPU & Memory",
        "31–70% CPU & Memory",
        "71–100% CPU & Memory"
    ]
}))

st.caption("Example: Heavy traffic → use values around 85–95%.")

# User Inputs
avg_memory = st.slider("Average Memory Usage", 0, 100, 65)
max_cpu = st.slider("Maximum CPU Usage", 0, 100 , 98)
max_memory = st.slider("Maximum Memory Usage", 0, 100 , 65)
assigned_memory = st.slider("Assigned Memory", 0, 100, 98)
failed = st.selectbox(
    "Previous Task Status",
    ["Successful", "Failed"]
)

failed = 0 if failed == "Successful" else 1


if st.button("Predict CPU Utilization"):

    sample = pd.DataFrame({
        "avg_memory": [avg_memory / 100],
        "max_cpu": [max_cpu / 100],
        "max_memory": [max_memory / 100],
        "assigned_memory": [assigned_memory / 100],
        "failed": [failed]
    })

    prediction = model.predict(sample)[0]
    cpu_percent = prediction * 100

    st.metric("Predicted CPU Utilization", f"{cpu_percent:.2f}%")

    if cpu_percent > 45:
        st.error("Scale Up: Add more virtual machines")
    elif cpu_percent < 20:
        st.success("Scale Down: Reduce unused resources")
    else:
        st.info("Keep Current Resources")