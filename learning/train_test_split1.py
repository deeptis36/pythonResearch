import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Step 1: Load the dataset
df = pd.read_csv('heart.csv')

# Step 2: Encode the categorical feature (Sex)
df_encoded = pd.get_dummies(df, columns=['Sex'], drop_first=True)

# Step 3: Define features and target variable
X = df_encoded.drop('HeartDisease', axis=1)  # Features
y = df_encoded['HeartDisease']                # Target

# Step 4: Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Scale the features

# Step 5: Split the dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 6: Initialize the Logistic Regression model
model = LogisticRegression(max_iter=200)

# Step 7: Train the model using the training data
model.fit(X_train, y_train)

# Step 8: Make predictions on the test data
y_pred = model.predict(X_test)

# Step 9: Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Step 10: Make predictions for new data
new_data = pd.DataFrame({
    'Age': [40], 
    'Cholesterol': [220], 
    'BloodPressure': [130], 
    'Sex_Male': [1]  # Corrected here
})

# Scale the new data
new_data_scaled = scaler.transform(new_data)  # Scale new data using the same scaler

# Make the prediction
prediction = model.predict(new_data_scaled)  # Use the scaled new data for prediction
print("Prediction for Age 30, Cholesterol 220, Blood Pressure 130, Male:", prediction[0])
