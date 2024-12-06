import re
from spellchecker import SpellChecker
import spacy

# Load spaCy model
nlp = spacy.load('en_core_web_md')

# Initialize SpellChecker
spell = SpellChecker()

# Define global arrays and keywords
from data import month_array, software_tools, skill_array, resume_classification, work_keywords, roles_array

employer_keywords = [
    "Ltd", "Pvt Ltd", "Private Limited", "Inc", "Inc.", "Corporation", "Corp", "LLC",
    "Life", "LLP", "PLC", "Co.", "Company", "Solutions", "Consultants", "Consulting",
    "Management Consultants", "Management Services", "Services", "Technologies",
    "Tech", "Software", "IT", "Digital", "Group", "Industries", "Enterprises",
    "Holdings", "Ventures", "Works", "Innovations", "Systems", "Labs", "Networks",
    "Communications", "Global", "International", "Regional", "Capital", "Investments",
    "Partners", "Financial", "Development", "Design", "Creatives", "Manufacturing",
    "Productions", "Logistics", "Engineering", "University", "Groups"
]

skip_keywords = ["role:", "client:", "working in :", "test", "sr", "sr test"]

# Function to ignore unwanted text
def ignore_text(text):
    text_lower = text.lower()
    for skip_word in skip_keywords:
        if skip_word in text_lower:
            return True
    return False

# Extract client name using regex patterns
def extract_client_name(text):
    patterns = [
        r"(?i)client:\s([a-z0-9\s&]+),\s?[a-z\s]+(?:\s\d{4}.*)?",
        r"(?i)client:\s([a-z0-9\s&]+)"
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1).strip()
    return None


def is_employer_in_nlp(text, employer_keywords):
    doc = nlp(text)
    
    # Flags for detection
    has_proper_noun = any(token.pos_ == "PROPN" for token in doc)
    has_gpe = any(ent.label_ == "GPE" for ent in doc.ents)
    has_employer_keyword = any(keyword.lower() in text.lower() for keyword in employer_keywords)
    
    # Combine criteria
    if has_proper_noun and has_gpe:
        return True
    if has_employer_keyword:
        return True
    return False
# Extract employers from the text
def extract_employers_only(text):
    extracted_employers = set()
    
    # Check for client name
    client_name = extract_client_name(text)
    if client_name:
       
        extracted_employers.add(client_name)
        return list(extracted_employers)

    # Clean the text
    clean_text = re.sub(r'[^\w\s,.]', ' ', text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()

    # Regex pattern for employer keywords
    pattern = r'([\w\s]+(?:' + '|'.join(re.escape(keyword) for keyword in employer_keywords) + r')[\w\s]*)'
    match = re.search(pattern, clean_text, re.IGNORECASE)
    if match:
        extracted_employers.add(match.group(1).strip())
       
        return list(extracted_employers)
    else:
        result = is_employer_in_nlp(text, employer_keywords)
        if result:
            extracted_employers.add(text)
            return list(extracted_employers)


    return list(extracted_employers)

# Append new employer only if unique
def add_if_unique(existing_employers, new_employer):
    new_employer = new_employer.lower().strip()
    for existing in existing_employers:
        if new_employer in existing.lower() or existing.lower() in new_employer:
            return
    existing_employers.append(new_employer)

# Check if a text contains a role
def is_role(text):
    for word in text.split():
        if word in roles_array:
            return True
    return False

# Main function to process the resume text and extract employers
def get_employer(resume_text):
    employers = []
    if not resume_text:
        return ""

    for text in resume_text.split("|"):
        if ignore_text(text) or not text.strip() or len(text.split()) >= 15:
            continue
        if not is_role(text):
            new_employers = extract_employers_only(text)
            for employer in new_employers:
                add_if_unique(employers, employer)

    return " ".join(employers)
