import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample data (job descriptions and resumes)
data = {
    'job_description': [
        "Looking for a backend developer with expertise in Node.js, Express, and MongoDB. Knowledge of REST APIs is a plus.",
        "Looking for a PHP developer with experience in Laravel and MySQL.",
        "Hiring a data analyst with expertise in Python and SQL.",
        "Seeking a frontend developer familiar with React and CSS."
    ],
    'resume_text': [
     
        "Data analyst proficient in Python and SQL with a strong analytical background.",
        "Frontend developer with experience in React and modern JavaScript.",
        "Machine learning engineer with extensive knowledge in TensorFlow and deep learning.",
        "Experienced Java developer skilled in oracle and aws.",
        "Experienced PHP developer skilled in Laravel and MySQL.",
    ]
}

# Create a DataFrame with job descriptions and resumes
job_descriptions = data['job_description']
resumes = data['resume_text']

# Create a TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Combine job descriptions and resumes for vectorization
all_texts = job_descriptions + resumes

# Fit and transform the text data
tfidf_matrix = vectorizer.fit_transform(all_texts)

# Split the transformed data back into job descriptions and resumes
job_desc_matrix = tfidf_matrix[:len(job_descriptions)]
resume_matrix = tfidf_matrix[len(job_descriptions):]

# Compute the cosine similarity between each job description and resume
similarity_matrix = cosine_similarity(job_desc_matrix, resume_matrix)

# Find the index of the most similar resume for each job description
best_matches = np.argmax(similarity_matrix, axis=1)

# Output the most matched resume index for each job description
for i, best_match_idx in enumerate(best_matches):
    print(f"Job Description {i+1}: Best matched resume index is {best_match_idx}, Resume: {resumes[best_match_idx]}")

# Optional: Output similarity scores (for debugging or analysis)
print("\nSimilarity Matrix (Job Descriptions vs Resumes):")
print(similarity_matrix)
