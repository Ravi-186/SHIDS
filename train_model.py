import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("data/raw/data.csv")

X = df.drop("label", axis=1)
y = df["label"].map({"attack": 0, "normal": 1})

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained successfully!")