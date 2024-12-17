import re
from spellchecker import SpellChecker
import spacy
from data  import skill_array,company_names

# Load spaCy model
nlp = spacy.load('en_core_web_md')

# Initialize SpellChecker
spell = SpellChecker()

# Define global arrays and keywords
from data import month_array, software_tools, skill_array, resume_classification, work_keywords, roles_array

employer_keywords = [
    "Ltd", "Pvt Ltd", "Private Limited", "Inc", "Inc.", "Corporation", "Corp", "LLC"," bank of","Bank",
    "Life", "LLP", "PLC", "Co.", "Company", "Solutions", "Consultants", "Consulting",
    "Management Consultants", "Management Services", "Services", "Technologies",
    "Tech", "Software", "IT", "Digital", "Group", "Industries", "Enterprises",
    "Holdings", "Ventures", "Works", "Innovations", "Systems", "Labs", "Networks",
    "Communications", "Global", "International", "Regional", "Capital", "Investments",
    "Partners", "Financial", "Development", "Design", "Creatives", "Manufacturing",
    "Productions", "Logistics", "Engineering", "University", "Groups"
]


skip_keywords = ["software", "roles & responsibilities","responsibilities"]

skip_keywords = skip_keywords+ month_array + skill_array + resume_classification + work_keywords+roles_array
# Function to ignore unwanted text
def ignore_text(text):
    text_lower = text.lower()

    for company in company_names:        
        if re.search(rf'\b{re.escape(company.lower())}\b', text_lower):            
            return False
        
    if text_lower.startswith("client:"):
        return False
    words_in_line = text.split(",")
    for word in words_in_line:
        for skip_word in skip_keywords:
            if re.fullmatch(rf'\b{re.escape(skip_word)}\b', word):
                return True
    for skip_word in skip_keywords:            
        if re.search(rf'\b{re.escape(skip_word)}\b', text_lower):           
            return True

# Extract client name using regex patterns
def extract_client_name(text):
    patterns = [
        r"(?i)client:\s([a-z0-9\s&]+),\s?[a-z\s]+(?:\s\d{4}.*)?",
        r"(?i)client:\s([a-z0-9\s&]+)"
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            # print(match.group(1).strip())
            # print(text)
            return match.group(1).strip()
    return None

def is_valid_employer(employer_name):
   
    doc = nlp(employer_name)
    for token in doc:
        if token.pos_ in {"ADP", "VERB","ADP"}:
            return False
    return True

def is_employer_from_data(text):
   
   
    # print(text)
    for company in company_names:        
        if re.search(rf'\b{re.escape(company.lower())}\b', text):
              
            return company
    
    if text.strip() in company_names:
        return text
    for employer in company_names:
        if employer in text:  # Check if employer name is in the input text
            # Find and return the matched part of the text
            match = re.search(rf"\b{re.escape(employer)}\b", text)
            if match:
                
                return text[match.start():match.end()]  
    return False

def is_employer_in_nlp(text, employer_keywords):
    doc = nlp(text)
    is_valid = is_valid_employer(text)
    if not is_valid:
        return False
    # Flags for detection
    has_proper_noun = any(token.pos_ == "PROPN" for token in doc)
    has_gpe = any(ent.label_ == "GPE" for ent in doc.ents)
    has_employer_keyword = any(keyword.lower() in text.lower() for keyword in employer_keywords)
    # #print(has_employer_keyword)
    # Combine criteria
    if has_proper_noun and has_gpe:
        return True
    if has_employer_keyword:
        return True
    return False
# Extract employers from the text
def extract_employers_only(text):
    extracted_employers = set()
    employer_name = ""
    # Check for client name
    client_name = extract_client_name(text)
    if client_name:
        # #print(f"Client Name: {client_name}")
        employer_name = client_name
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
        employer_name = match.group(1).strip()
        is_vlid = is_valid_employer(employer_name)
        if is_vlid:
            #print(f"Matched Employer: {match.group(1).strip()}")
            return list(extracted_employers)
        
    result = is_employer_in_nlp(text, employer_keywords)

    if result:
        employer_name = text
        #print("NLP mployer", text)
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


def extract_employer_pattern_match(text):
    # Clean and normalize text
    clean_text = re.sub(r'[^\w\s,.]', '', text)  # Remove special characters
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()  # Normalize spaces
    
    # Refined regex pattern
    pattern = r'\b([\w\s]*\b(?:' + '|'.join(re.escape(keyword) for keyword in employer_keywords) + r')\b[\w\s]*)'
    match = re.search(pattern, clean_text, re.IGNORECASE)

    if match:
        employer_name = match.group(1).strip()
        return employer_name
    return None




def extract_employer_by_nlp(text) :
  
    doc = nlp(text)
 
   
    for ent in doc.ents:
       if ent.label_ in {"ORG", "GPE"}:
            return text
    # for token in doc:
    #     if token.pos_ == "PROPN":
    #         return text






import re

def extract_employers_only_new(text):
    # Clean the input text by removing special characters and normalizing spaces
    clean_text = re.sub(r'[^\w\s,.]', ' ', text)  # Remove special characters except for word characters, spaces, commas, and periods.
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()  # Normalize spaces to a single space and strip leading/trailing spaces.
    
    employer_name = []  # Initialize an empty list to store employer names.
    
    # Helper function to ensure each value is a string and avoid duplicates
    def add_if_string(name):
        if isinstance(name, str):  # Only add if the name is a string
            if name and name not in employer_name:  # Avoid duplicates and ensure non-empty string
                employer_name.append(name)
        elif isinstance(name, list):  # If the name is a list, add its items if they're strings
            for item in name:
                add_if_string(item)
    
    # Try extracting the client/employer name using various methods
    client_name = is_employer_from_data(text)
    if client_name:
        # print("is_employer_from_data:", client_name)
        add_if_string(client_name)
        return client_name

    client_name = extract_client_name(text)
    if client_name:
        # print("extract_client_name:", client_name)
        add_if_string(client_name)
        return client_name

    client_name = extract_employer_pattern_match(text)
    add_if_string(client_name)

    client_name = extract_employer_by_nlp(text)
    if client_name:
        # print("extract_employer_by_nlp:", client_name)
        add_if_string(client_name)
        return client_name

    # client_name = extract_employers_only(text)
    # if client_name:
    #     # print("extract_employers_only:", client_name)
    #     add_if_string(client_name)
    #     return client_name
    
    # Join the list of employer names as a string, separated by commas.
    employer_name_str = ', '.join(employer_name) if employer_name else ''
    
    # Return the final string with employer names.
    return employer_name_str
     
# Main function to process the resume text and extract employers
def get_employer(resume_text):
   
    # clean_text = re.sub(r'[^\w\s,.]', ' ', resume_text) 
    # clean_text = re.sub(r'[^\w\s.]', ' ', clean_text)
    # clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    # resume_text = clean_text
    resume_text = re.sub(r'[^\w\s,]', ' ', resume_text)
    employers = []
    new_employers =""
    if not resume_text:
        return ""
    pipe_split = resume_text.split("|")
    broken_text = []
    # for segment in pipe_split:
    #     # broken_text.extend(segment.split(","))
    #     broken_text.extend(segment)
   
    
    for text in pipe_split:
       
        if ignore_text(text) or not text.strip() or len(text.split()) >= 14:         
            continue

        if not is_role(text):
            new_employers = extract_employers_only_new(text)
            # print(f"extracted employer from resume: {new_employers}")
            new_employers = new_employers.strip()
            new_employers = re.sub(r'^\s*,\s*', '', new_employers)
            # print(f"extracted employer from resume: {new_employers}")
            # new_employers = re.sub(r'\s+(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)\s*$', '', new_employers, flags=re.IGNORECASE)

           
            new_employers = re.sub(r'\s+', ' ', new_employers.strip())  # Normalize whitespace
            new_employers = re.sub(
                r'[,\s]+(january|february|march|april|may|june|july|august|september|october|november|december|'
                r'jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[,.\s]*$',
                '',
                new_employers,
                flags=re.IGNORECASE
            )
            new_employers = re.sub(r'\bto\b', '', new_employers, flags=re.IGNORECASE)
            words = new_employers.strip().split()

            # Check if the last word is in month_array
            if words and words[-1] in month_array:
                # Remove the last word if it is in month_array
                new_employers = ' '.join(words[:-1])
            # print(f"removed month from new_employers: {new_employers}")
    return new_employers

