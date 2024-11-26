import re
import spacy
import pdfplumber
import docx

# Load the SpaCy model (ensure you have a model installed, e.g., 'en_core_web_sm')
nlp = spacy.load('en_core_web_sm')

# Helper function to extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# Helper function to extract text from DOCX
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

# Clean name function
def clean_name(name):
    # Remove everything after the first newline character
    name = name.split('\n')[0]
    
    # Remove any special characters (anything that's not a letter or space)
    cleaned_name = re.sub(r'[^a-zA-Z\s]', '', name)
    
    # Return None if the cleaned name is empty, else return the cleaned name
    return cleaned_name.strip() if cleaned_name.strip() else None

# Define a list of common skills
known_skills = [
    "Python", "Java", "C++", "JavaScript", "SQL", "HTML", "CSS", "Machine Learning",
    "Deep Learning", "Data Analysis", "Project Management", "Excel", "Git", "Laravel",
    "Angular", "React", "Django", "Flask", "Node.js", "AWS", "Azure", "Docker", "Kubernetes"
]

# Function to extract skills
def extract_skills(text):
    skills_found = []
    for skill in known_skills:
        # Use regex to find whole word matches only
        if re.search(rf'\b{re.escape(skill)}\b', text, re.IGNORECASE):
            skills_found.append(skill)
    return skills_found
# Function to parse resume sections
def parse_resume(text):
    doc = nlp(text)
    data = {
        "name": None,
        "email": None,
        "phone": None,
        "education": [],
        "experience": [],
        "organizations": extract_org(text)
    }
    
    # Regex patterns for email and phone
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'\+?\d[\d\s-]{8,}\d'

    # Extract email and phone
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    if emails:
        data['email'] = emails[0]
    if phones:
        data['phone'] = phones[0]

    # Extract name using NER (first PERSON entity)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            data['name'] = clean_name(ent.text)
            break

    # Further parsing for education, experience, and skills can be added here

    return data

def extract_org(text):
    ORG = []
    doc = nlp(text)
    skills = []
    for ent in doc.ents:
        print(ent.text, ent.label_)
        if ent.label_ == "ORG":
            ORG.append(ent.text)
    return ORG

# Load resume text based on file type
file_path = "resume.pdf"  # Replace with the path to your resume
file_type = "pdf"  # Change to "docx" if using a DOCX file

if file_type == "pdf":
    resume_text = extract_text_from_pdf(file_path)
elif file_type == "docx":
    resume_text = extract_text_from_docx(file_path)
else:
    raise ValueError("Unsupported file type. Use 'pdf' or 'docx'.")

# Parse the resume
parsed_data = parse_resume(resume_text)
print(parsed_data)
