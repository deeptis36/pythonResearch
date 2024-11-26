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
        "Seeking a front-end developer with expertise in HTML, CSS, and JavaScript.",
        "We need a data scientist skilled in Python, Machine Learning, and Data Analysis.",
        "Looking for a full-stack developer proficient in React, Node.js, and MongoDB.",
        "Seeking a backend engineer with experience in Django, PostgreSQL, and AWS.",
        "Looking for a software engineer familiar with DevOps practices and cloud computing.",
        "Hiring for a Java developer with SpringBoot and Microservices experience."
    ],
    'skills': [
        "PHP, Laravel, MySQL",
        "HTML, CSS, JavaScript",
        "Python, Machine Learning, Data Analysis",
        "React, Node.js, MongoDB",
        "Django, PostgreSQL, AWS",
        "DevOps, Cloud Computing",
        "Java, SpringBoot, Microse rvices"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)
print(df)

print("========================================================================================================")
print(df.shape)
print("========================================================================================================")

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['job_description'], df['skills'], test_size=0.1, random_state=10)

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

print("pipeline.decision_function(X_test):")
print(pipeline.decision_function(X_test))
print("--------------------------------------------------------------------------------------")

print("pipeline.score(X_test, y_test):")
print(pipeline.score(X_test, y_test))
print("--------------------------------------------------------------------------------------")

# print(classification_report(y_test, predictions, zero_division=1))  # Avoids the undefined warnings
