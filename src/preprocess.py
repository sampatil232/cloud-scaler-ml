import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../data/cleaned_cluster_data.csv")

# Features
X = df[[
    "avg_memory",
    "max_cpu",
    "max_memory",
    "assigned_memory",
    "failed"
]]

# Target
# preprocess.py
y = df["avg_cpu"] / df["avg_cpu"].max()

# Save processed data
X.to_csv("../data/X.csv", index=False)
y.to_csv("../data/y.csv", index=False)

print("Preprocessing completed!")

