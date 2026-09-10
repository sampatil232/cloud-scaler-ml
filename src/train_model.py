import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load data
X = pd.read_csv("../data/X.csv")
y = pd.read_csv("../data/y.csv").squeeze()

print(X.isnull().sum())

# Combine X and y
data = X.copy()
data["avg_cpu"] = y

# Remove rows containing NaN
data = data.dropna()

# Separate again
X = data.drop("avg_cpu", axis=1)
y = data["avg_cpu"]

print(X.isnull().sum())


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training:", X_train.shape)
print("Testing :", X_test.shape)

# Models
models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, random_state=42)
}

# Train and evaluate
for name, model in models.items():

    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, pred)
    rmse = mean_squared_error(y_test, pred) ** 0.5
    r2 = r2_score(y_test, pred)

    print("\n", name)
    print("-" * 30)
    print("MAE :", round(mae, 6))
    print("RMSE:", round(rmse, 6))
    print("R²  :", round(r2, 6))


# Save Random Forest model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

joblib.dump(rf_model, "../models/random_forest.pkl")

print("\nModel saved successfully!")