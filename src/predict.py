import joblib
import pandas as pd

# Load trained model
model = joblib.load("../models/random_forest.pkl")

# Sample input
sample = pd.DataFrame({
    "avg_memory": [0.04],
    "max_cpu": [0.18],
    "max_memory": [0.07],
    "assigned_memory": [0.08],
    "failed": [0]
})

# Predict CPU utilization
prediction = model.predict(sample)

print(f"Predicted CPU Utilization: {prediction[0] * 100:.2f}%")

# Auto-scaling decision
cpu = prediction[0] * 100

if cpu > 75:
    print("Recommendation: SCALE UP")
elif cpu < 40:
    print("Recommendation: SCALE DOWN")
else:
    print("Recommendation: KEEP CURRENT RESOURCES")