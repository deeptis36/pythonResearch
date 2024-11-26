from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score                                      

# Step 1: Load the data
df = pd.read_csv('salary.csv')

# Step 2: Features and target variable
X = df[['Age', 'Salary']]  # Features
y = df['Purchased']        # Target

# Step 3: Splitting the dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Initialize the Logistic Regression model
model = LogisticRegression()

# Step 5: Train the model using the training data
model.fit(X_train, y_train)

# Step 6: Make predictions on the test data
y_pred = model.predict(X_test)

print(y_pred)
# Step 7: Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Step 8: Make predictions for new data (e.g., Age = 22, Salary = 780000)
new_data = pd.DataFrame({'Age': [25], 'Salary': [178000]})
prediction = model.predict(new_data)
print("Prediction for Age 82 and Salary 780000:", prediction[0])

# Print the train and test sets
# print("X_train:\n", X_train)
# print("X_test:\n", X_test)
