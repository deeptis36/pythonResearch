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
    if text_lower.startswith("client:"):
        return False
    words_in_line = text.split(",")
    for word in words_in_line:
        if word in skip_keywords:
            # print("skip_keywords",text)
            return True
    for skip_word in skip_keywords:
        if skip_word in text_lower:
            # print("TEXT LOWER",text)
            return True
    # if not is_valid_employer(text):
    #     returnBoeing

# Extract client name using regex patterns
def extract_client_name(text):
    patterns = [
        r"(?i)client:\s([a-z0-9\s&]+),\s?[a-z\s]+(?:\s\d{4}.*)?",
        r"(?i)client:\s([a-z0-9\s&]+)"
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            print(match.group(1).strip())
            print(text)
            return match.group(1).strip()
    return None

def is_valid_employer(employer_name):
   
    doc = nlp(employer_name)
    for token in doc:
        if token.pos_ in {"ADP", "VERB","ADP"}:
            return False
    return True

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

def extract_employers_only_new1(text):
    clean_text = re.sub(r'[^\w\s,.]', ' ', text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    client_name = ""
    employer_name = []
    client_name = extract_client_name(text)
    if client_name:
        return client_name
        employer_name.append(client_name)
      
    client_name = extract_employer_pattern_match(text)
    if client_name :
        return client_name
        employer_name.append(client_name)
    

    client_name = extract_employer_by_nlp(text)
    if client_name :
        return client_name
        employer_name.append(client_name)



    client_name = extract_employers_only(text)
    if client_name :
        return client_name
    return employer_name





def extract_employers_only_new(text):
   
    clean_text = re.sub(r'[^\w\s,.]', ' ', text)  # Remove special characters except for word characters, spaces, commas, and periods.
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()  # Normalize spaces to a single space and strip leading/trailing spaces.
    
    employer_name = []  # Initialize an empty list to store employer names.
    
    # Helper function to ensure each value is a string
    def add_if_string(name):
        if isinstance(name, str):  # Only add if the name is a string
            if name not in employer_name:  # Avoid duplicates
                employer_name.append(name)
        elif isinstance(name, list):  # If the name is a list, add its items if they're strings
            for item in name:
                add_if_string(item)
    
    # Extract client name using different methods and add if valid.
   
    client_name = extract_client_name(text)
    
    add_if_string(client_name)
    if client_name:
        print("client name", client_name)
        employer_name.append(client_name)
        employer_name_str = ', '.join(employer_name) if employer_name else ''
        return client_name
    client_name = extract_employer_pattern_match(text)
    add_if_string(client_name)
    
    client_name = extract_employer_by_nlp(text)
    add_if_string(client_name)
    
    client_name = extract_employers_only(text)
    add_if_string(client_name)
    
    # Join the list of employer names as a string, separated by commas.
    employer_name_str = ', '.join(employer_name) if employer_name else ''
    
    # Debugging print statement: print the string instead of the list.
    # print(f"EMPLOYER: {employer_name_str}\n")
   
    
    # Return the final string with employer names.
    return employer_name_str

        
# Main function to process the resume text and extract employers
def get_employer(resume_text):
   
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
            # #print(f"Text: {text}\n")
            new_employers = extract_employers_only_new(text)
            print(new_employers)
            # for employer in new_employers:
            #     add_if_unique(employers, employer)
    # return ""
    return new_employers

