import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Example resumes (lists of skills)
resumes = [
    {'resume_id': 'resume1', 'resume': 'Python, Django, HTML, CSS', 'label': 1},
    {'resume_id': 'resume2', 'resume': 'Java, Spring, Hibernate, MySQL', 'label': 0},
    {'resume_id': 'resume3', 'resume': 'JavaScript, React, Node.js, Express', 'label': 1},
    {'resume_id': 'resume4', 'resume': 'C#, .NET, SQL Server, Azure', 'label': 0},
    {'resume_id': 'resume5', 'resume': 'Python, Flask, Machine Learning, Pandas', 'label': 1},
]

# Convert to DataFrame
df = pd.DataFrame(resumes)

# Preprocess resumes (basic transformation: count how many known skills appear in each resume)
skills = ['Python', 'Java', 'JavaScript', 'C#', 'HTML', 'CSS', 'React', 'Node.js', 'Machine Learning', 'Django']

# Create a feature matrix where each column represents a skill
for skill in skills:
    df[skill] = df['resume'].apply(lambda x: 1 if skill in x else 0)

# Features (skills) and labels
X = df[skills]  # Skills matrix
y = df['label']  # Target labels (job match or not)
resume_ids = df['resume_id']  # Resume IDs

# Split the data into training and testing sets with a smaller test size
X_train, X_test, y_train, y_test, resume_ids_train, resume_ids_test = train_test_split(X, y, resume_ids, test_size=0.2, random_state=42)

# Initialize a RandomForest model with tuned hyperparameters
model = RandomForestClassifier(n_estimators=10, max_depth=3, random_state=42)

# Train the model (fit it to the training data)
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the model (accuracy score)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Return the resume IDs alongside the predictions and true labels
results = pd.DataFrame({
    'resume_id': resume_ids_test,
    'predicted_label': y_pred,
    'actual_label': y_test
})

print(results)
