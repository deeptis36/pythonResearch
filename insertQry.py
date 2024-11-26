
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",  # Change to your host
    user="root",  # Change to your MySQL username
    password="password",  # Change to your MySQL password
    database="job"  # Change to your database name
)

skills_database = [
    'data science', 'machine learning', 'python', 'data analysis', 'statistical analysis','laravel','php',
    'project management', 'java', 'javascript', 'sql', 'aws', 'docker', 'kubernetes', 'cloud architecture',
    'penetration testing', 'neural networks', 'natural language processing', 'ios', 'android', 'full-stack development',
    'react', 'node.js', 'seo', 'social media management' , 'Digital marketing',
]
cursor = conn.cursor()

# Insert each skill into the 'skills' table
insert_query = "INSERT INTO skills (name) VALUES (%s)"
for skill in skills_database:
    cursor.execute(insert_query, (skill,))

# Commit the transaction to save changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Skills inserted successfully!")