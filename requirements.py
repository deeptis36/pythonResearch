import spacy
from fuzzywuzzy import process

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Predefined list of skills
skills_database = [
    'data science', 'machine learning', 'python', 'data analysis', 'statistical analysis',
    'laravel', 'php', 'project management', 'java', 'javascript', 'sql', 'aws',
    'docker', 'kubernetes', 'cloud architecture', 'penetration testing', 
    'neural networks', 'natural language processing', 'ios', 'android', 
    'full-stack development', 'react', 'node.js', 'seo', 'social media management', 
    'digital marketing','artificial intelligence'
] 

def extract_skills(text, user_skills=[], threshold=80):
    # Ensure user_skills is a list
    user_skills = list(user_skills)

    # Combine predefined skills with user-defined skills
    combined_skills = set(skills_database + user_skills)

    # Tokenize and process the text
    doc = nlp(text)
    
    # Create a set to store the found skills
    found_skills = set()

    # Check each token in the text
    for token in doc:
        # Lemmatize the token
        lemma = token.lemma_.lower()

        # Skip empty strings and punctuation
        if lemma and lemma.isalpha():  # Ensure lemma is not empty and is alphabetic
            # Perform fuzzy matching
            matched_skill, score = process.extractOne(lemma, combined_skills)

            # Check if the score meets the threshold for a match
            if score >= threshold:
                found_skills.add(matched_skill)

    return found_skills

# Example job requirement text with potential misspellings
job_requirement_text = """
We are looking for a Data Scientist who is proficient in python and has experience with machine learning algorithms.
The candidate should be able to analyze large datasets and create predictive models using frameworks like Django and Flask.
"""

# User-defined skills
resume_text = """
I am a Data Scientist with expertise in python and machine learning algorithms. 
I have experience in data analysis, statistical analysis, and I have worked with frameworks like Django and Flask.
I also have knowledge in data science and artaficial intellience.
"""

# Extract user-defined skills from the resume text
user_defined_skills = extract_skills(resume_text)
print("******Extracted User Defined Skills:*******************")
for skill in user_defined_skills:
    print(skill)
print("=========================================================================================")
print("****SKILL WE FOUND ******")
# Extract skills from the job requirement text using the user-defined skills
skills_found = extract_skills(job_requirement_text, user_defined_skills)

# Display the found skills
print("Extracted Skills:")
for skill in skills_found:
    print(skill)
