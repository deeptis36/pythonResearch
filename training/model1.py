from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the Iris dataset
data = load_iris()

X = data.data   # Features
y = data.target # Labels (Classes)

print(X)
print(y)
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize a model (Random Forest in this case)
model = RandomForestClassifier()

# Train the model (fit it to the training data)
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)
print(y_pred)
print(y_test)
# Evaluate the model (accuracy score)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
