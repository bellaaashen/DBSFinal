# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C_z8OUwjBYJ_d6nHa5247PUFSSiapb_6
"""

# Step 1: Model training and recommendation logic using KNN and Random Forest

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
import pandas as pd
import random

# Load the dataset
file_path = 'extended_synthetic_insurance_data.csv'
insurance_data = pd.read_csv(file_path)

# Select relevant features and simulate ProductID as target
features = ['age', 'smoker', 'claim_amount']
insurance_data['ProductID'] = random.choices(range(1, 11), k=len(insurance_data))

# Extract features and target
X = insurance_data[features]
y = insurance_data['ProductID']

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Initialize models
knn = KNeighborsClassifier(n_neighbors=5)
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Combine KNN and Random Forest in a Voting Classifier
ensemble_model = VotingClassifier(estimators=[('knn', knn), ('rf', rf)], voting='hard')

# Train the ensemble model
ensemble_model.fit(X_scaled, y)

# Define the recommendation function
def recommend_products(input_features):
    input_scaled = scaler.transform([input_features])
    predicted_product = ensemble_model.predict(input_scaled)
    return predicted_product

# Example recommendation
example_input = [30, 1, 5000]  # Age: 30, Smoker: Yes (1), Claim Amount: $5000
recommendation = recommend_products(example_input)
recommendation