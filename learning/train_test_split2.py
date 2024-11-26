import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Step 1: Load the actual dataset
df = pd.read_csv('heart.csv')

# Step 2: Encode the categorical feature (Gender)
df_encoded = pd.get_dummies(df, columns=['Gender'], drop_first=True)

# Step 3: Define features and target variable
X = df_encoded.drop('HeartDisease', axis=1)  # Features
y = df_encoded['HeartDisease']                # Target

# Step 4: Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 5: Split the dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 6: Initialize the Logistic Regression model
model = LogisticRegression()

# Step 7: Train the model using the training data
model.fit(X_train, y_train)

# Step 8: Make predictions on the test data
y_pred = model.predict(X_test)

# Step 9: Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Step 10: Make predictions for new data
# Only include Gender_Male because 'Gender_Female' was dropped during encoding
new_data = pd.DataFrame({
    'Age': [5], 
    'Cholesterol': [200], 
    'BloodPressure': [110], 
    'Gender_Male': [0]  # Ensure the same columns as training data
})

# Scale the new_data to match the training data scaling0
new_data_scaled = scaler.transform(new_data)

# Make predictions using the model
prediction = model.predict(new_data_scaled)
print(new_data)
print("___________________________________")
print()
print("Heart disease possibility:", "Yes" if prediction[0] == 1 else "No")
print("____________________________________")


