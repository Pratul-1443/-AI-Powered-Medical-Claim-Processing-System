# import these

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample dataset (You can replace this with real invoice data)
data = {
    "amount": [500, 1000, 200, 700, 1500],
    "diagnosis_code": [101, 202, 303, 101, 404],
    "is_fraudulent": [0, 1, 0, 1, 0]  # 0 = valid, 1 = fraudulent
}
# Convert dictionary to pandas DataFrame

df = pd.DataFrame(data)
# Split the data into training and testing sets

X = df.drop(columns=["is_fraudulent"])
y = df["is_fraudulent"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Create a RandomForest model

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
# Save the trained model for later use

joblib.dump(model, "claim_classifier.pkl")

print("Model training complete. Model saved as claim_classifier.pkl")
