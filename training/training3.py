import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# Updated dataset (expand this with more samples for better accuracy)
data = {
    'job_description': [
        "Looking for a PHP developer with experience in Laravel and MySQL.",
        "Hiring a data analyst with expertise in Python and SQL.",
        "Seeking a frontend developer familiar with React and CSS.",
        "Looking for a machine learning engineer with experience in TensorFlow."
    ],
    'resume_text': [
        "Experienced PHP developer skilled in Laravel and MySQL.",
        "Data analyst proficient in Python and SQL with a strong analytical background.",
        "Frontend developer with experience in React and modern JavaScript.",
        "Machine learning engineer with extensive knowledge in TensorFlow and deep learning."
    ],
    'match': [1, 1, 1, 1]  # All resumes match their respective job descriptions
}

# Create a DataFrame
df = pd.DataFrame(data)

# Assume that you have non-matching resumes as well for better training
# Add some non-matching resumes
non_matching_data = {
    'job_description': [
        "Looking for a PHP developer with experience in Laravel and MySQL.",
        "Hiring a data analyst with expertise in Python and SQL.",
        "Seeking a frontend developer familiar with React and CSS."
    ],
    'resume_text': [
        "Project manager with experience in managing teams and projects.",
        "Customer support representative with excellent communication skills.",
        "Graphic designer with a passion for creating visual content."
    ],
    'match': [0, 0, 0]  # No match for these
}

# Combine both matching and non-matching data
combined_data = data['job_description'] + non_matching_data['job_description']
combined_resumes = data['resume_text'] + non_matching_data['resume_text']
combined_labels = data['match'] + non_matching_data['match']

# Create a DataFrame with all data
combined_df = pd.DataFrame({
    'job_description': combined_data,
    'resume_text': combined_resumes,
    'match': combined_labels
})

# Splitting the data into features and labels
X = combined_df['job_description'] + " " + combined_df['resume_text']  # Combine job desc and resume text
y = combined_df['match']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

# Create a pipeline for the model
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),  # Convert text to TF-IDF features
    ('classifier', LogisticRegression(max_iter=1000))  # Logistic Regression classifier
])

# Train the model
pipeline.fit(X_train, y_train)

# Predictions
predictions = pipeline.predict(X_test)

# Evaluation with zero_division set to handle undefined metrics
print("x train:")
print(X_train)
print("--------------------------------------------------------------------------------------")
print("x test:")
print(X_test)
print("--------------------------------------------------------------------------------------")
print("y train:")
print(y_train)
print("--------------------------------------------------------------------------------------")
print("y test:")
print(y_test)
print("--------------------------------------------------------------------------------------")
print("predictions:")
print(predictions)
print("--------------------------------------------------------------------------------------")

# Display classification report with zero_division parameter
print("Classification Report:")
print(classification_report(y_test, predictions, zero_division=0))  # Set zero_division=0 or 1 based on your preference

print("--------------------------------------------------------------------------------------")
print("pipeline.score(X_test, y_test):")
print(pipeline.score(X_test, y_test))
print("--------------------------------------------------------------------------------------")

# Inspect the unique predictions
print("Unique Predictions:")
print(set(predictions))
