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


# Load SpaCy model
nlp = spacy.load("en_core_web_sm")


# Predefined skill set for matching
cursor = conn.cursor()

# Define the SELECT query to retrieve skills
select_query = "SELECT * FROM skills"

# Execute the query
cursor.execute(select_query)

# Fetch all the rows from the query result
skills = cursor.fetchall()

# Initialize an array to store the skills
skills_database = []

# Store fetched skills in the skills_database array
for skill in skills:
    skills_database.append(skill[1])  # Assuming skill[1] contains the skill name

# Display the skills stored in the array
print("Skills database:", skills_database)

# Function for text preprocessing
def preprocess_text(text):
    """
    Preprocesses the text by tokenizing, lemmatizing, and removing stop words and punctuations.

    Parameters:
    text (str): The text to preprocess (either resume or job description).

    Returns:
    List[str]: Cleaned and preprocessed list of tokens.
    """
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct and len(token) > 1]
    return " ".join(tokens)

# Function to find matched skills from a predefined skills list
def extract_skills(preprocessed_text, skills_database):
    """
    Extracts the matched skills based on a predefined skill set.

    Parameters:
    preprocessed_text (str): Preprocessed job description or resume text.
    skills_database (List[str]): Predefined set of skills to match.

    Returns:
    List[str]: Matched skills
    """
    matched_skills = [skill for skill in skills_database if skill in preprocessed_text]
    return matched_skills

# Array of resumes for testing
resumes = [
    "Experienced Data Scientist with a strong background in machine learning, data analysis, and Python programming.",
    "Software Developer with 5 years of experience in full-stack web development using JavaScript, React, and Node.js.",
    "Project Manager with experience in overseeing large-scale IT projects, ensuring timely delivery and budget management.",
    "Experienced in php laravel with 5 year experience.",
    "Experienced Data Scientist with a strong background in machine learning, data analysis, and Python programming.",
    "Software Developer with 5 years of experience in full-stack web development using JavaScript, React, and Node.js.",
    "Project Manager with experience in overseeing large-scale IT projects, ensuring timely delivery and budget management.",
    "Marketing Specialist skilled in digital marketing, content creation, SEO, and social media management.",
    "Senior Data Analyst with expertise in SQL, Python, and Tableau for data visualization and business insights.",
    "Cloud Engineer proficient in AWS, Docker, Kubernetes, and cloud architecture design and deployment.",
    "Cybersecurity Analyst with a focus on network security, penetration testing, and vulnerability assessments.",
    "AI Engineer experienced in developing machine learning models, neural networks, and natural language processing solutions.",
    "Business Analyst skilled in process improvement, stakeholder management, and data-driven decision-making.",
    "Mobile App Developer with expertise in iOS and Android development, Swift, Kotlin, and cross-platform solutions."
]

# Predefined job description for comparison
job_description = "We required laravel/php web developer with 5 years of experience."

# Preprocess the job description
preprocessed_job = preprocess_text(job_description)

# Extract skills from the job description
job_skills = extract_skills(preprocessed_job, skills_database)

# Preprocess all resumes and extract their skills
preprocessed_resumes = [preprocess_text(resume) for resume in resumes]
resume_skills = [extract_skills(resume, skills_database) for resume in preprocessed_resumes]

# Combine job skills and resume skills into a corpus for TF-IDF vectorization
corpus = [" ".join(job_skills)] + [" ".join(skills) for skills in resume_skills]

# Vectorize text using TF-IDF
vectorizer = TfidfVectorizer()

# Fit and transform the corpus to a TF-IDF representation
X = vectorizer.fit_transform(corpus)

# Calculate cosine similarity between the job description and each resume
similarity_matrix = cosine_similarity(X)

# Output the match percentage and matched/missing skills for each resume
for i in range(1, len(resumes) + 1):
    match_percentage = similarity_matrix[0][i] * 100
    matched_skills = resume_skills[i - 1]
    missing_skills = set(job_skills) - set(matched_skills)
    
    print(f"Resume {i}: {match_percentage:.2f}% match")
    print(f"Matched Skills: {', '.join(matched_skills) if matched_skills else 'No matched skills'}")
    print(f"Missing Skills: {', '.join(missing_skills) if missing_skills else 'No missing skills'}\n")
