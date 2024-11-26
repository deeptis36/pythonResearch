import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

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
    return tokens

# Function to calculate matched skill set
def get_matched_skills(preprocessed_job, preprocessed_resume):
    """
    Finds the common skills (tokens) between the job description and a resume.

    Parameters:
    preprocessed_job (List[str]): Preprocessed job description tokens.
    preprocessed_resume (List[str]): Preprocessed resume tokens.

    Returns:
    List[str]: Common skills between the job description and the resume.
    """
    return set(preprocessed_job).intersection(set(preprocessed_resume))

def get_skill_sets(preprocessed_job, preprocessed_resume):
    """
    Finds the common (matched) and missing (required) skills between the job description and a resume.

    Parameters:
    preprocessed_job (List[str]): Preprocessed job description tokens.
    preprocessed_resume (List[str]): Preprocessed resume tokens.

    Returns:
    Tuple[List[str], List[str]]: (Matched skills, Missing skills)
    """
    job_set = set(preprocessed_job)
    resume_set = set(preprocessed_resume)
    matched_skills = job_set.intersection(resume_set)
    missing_skills = job_set.difference(resume_set)
    return matched_skills, missing_skills

# Array of 10 resumes for testing
resumes = [
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
job_description = """
    We are seeking a data scientist with expertise in machine learning, statistical analysis, and proficiency in Python.
    The candidate should have experience in developing data-driven models and working with large datasets.
"""

# Preprocess the job description
preprocessed_job = preprocess_text(job_description)

# Preprocess all resumes and store them in an array
preprocessed_resumes = [preprocess_text(resume) for resume in resumes]

# Vectorize text using TF-IDF
vectorizer = TfidfVectorizer()

# Combine job description and all resumes into a single corpus
corpus = [" ".join(preprocessed_job)] + [" ".join(resume) for resume in preprocessed_resumes]

# Fit and transform the corpus to a TF-IDF representation
X = vectorizer.fit_transform(corpus)

# Calculate cosine similarity between the job description and each resume
similarity_matrix = cosine_similarity(X)

# Extract match percentages and matched skills for each resume
print("Match percentages and matched skill sets between the job description and each resume:\n")
for i in range(1, len(resumes) + 1):
    match_percentage = similarity_matrix[0][i] * 100
    matched_skills = get_matched_skills(preprocessed_job, preprocessed_resumes[i - 1])
    matched_skills, missing_skills = get_skill_sets(preprocessed_job, preprocessed_resumes[i - 1])
    print(f"Resume {i}: {match_percentage:.2f}% match")
    print(f"Matched Skills: {', '.join(matched_skills) if matched_skills else 'No matched skills'}")   
    print(f"Missing Skills: {', '.join(missing_skills) if missing_skills else 'No missing skills'}")
    print("\n")