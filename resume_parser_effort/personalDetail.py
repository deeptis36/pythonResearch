import re
import fitz  # PyMuPDF
import docx
import os
import spacy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
nlp = spacy.load("en_core_web_sm")

def extract_name_using_spacy(text):
    # Process the text with spaCy
    doc = nlp(text)
    
    # Extract named entities labeled as persons
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def is_proper_noun(name):
    """Check if the name consists of proper nouns (each word starts with a capital letter)."""
    words = name.split()
    return all(word[0].isupper() for word in words)

def is_paragraph(text):
    """Check if the text seems like a paragraph based on length and content."""
    return len(text.split()) > 5 and bool(re.search(r'[.!?]', text))

def classify_text(text):
    """Classify whether the text is a name, paragraph, or something else."""
    cleaned_text = text.strip()

    if is_proper_noun(cleaned_text):
        return "Name"
    elif is_paragraph(cleaned_text):
        return "Paragraph"
    else:
        return "Something Else"

def extract_email(resume_text):
    """Extract email address from resume text."""
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email = re.search(email_pattern, resume_text)
    return email.group(0).strip() if email else None

def extract_phone(resume_text):
    """Extract phone number from resume text."""
    phone_pattern = r'\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,4}'
    phone = re.search(phone_pattern, resume_text)
    return phone.group(0).strip() if phone else None

def extract_address(resume_text):
    """Extract address from resume text."""
    address_pattern = r'\d{1,5}\s\w+(\s\w+){2,}'
    address = re.search(address_pattern, resume_text)
    return address.group(0).strip() if address else None

def extract_name_from_resume(resume_text):
    name_pattern = r"\b([A-Z][a-z]+(?: [A-Z][a-z]+)?)\b"  # Matches first and last names
    potential_names = re.findall(name_pattern, resume_text)
    
    # Filter out very short names
    potential_names = [name for name in potential_names if len(name.split()) > 1]
    return potential_names

def match_name_to_list(name_part, match_list, threshold=80):
    best_match = process.extractOne(name_part, match_list, scorer=fuzz.partial_ratio)
    if best_match and best_match[1] >= threshold:
        return best_match[0]
    return None

def confirm_name(name, extracted_name_list, email):
    # Ensure the email is a string, not a tuple
    email = email[0] if isinstance(email, tuple) else email  # Check if email is a tuple and extract the string if it is
    
    # Check if email is None before attempting to split
    if email:
        # Extract the name part from the email before '@'
        name_part_from_email = email.split('@')[0]
        
        # Print the name, extracted list, and the email part
        # print("Name:", name)
        # print("Extracted Name List:", extracted_name_list)
        # print("Extracted Email Part:", name_part_from_email)
        
        # Call the function to match the email name part with the names in the list
        closed_matched_name = match_name_to_list(name_part_from_email, extracted_name_list)
        
        # Check if a match was found
        if closed_matched_name:
            return closed_matched_name
        else:
            return name
        
        
    else:
       
        return name


def extract_name(resume_text):
    lines = resume_text.strip().split('\n')
    first_line = lines[0].strip()

    if '|' in first_line:
        first_line = first_line.split('|')[0].strip()

    if ',' in first_line:
        first_line = first_line.split(',')[0].strip()

    name_pattern = r"^[^:]+(?=\s*Email:)"
    match = re.search(name_pattern, first_line)

    if match:
        first_line = match.group(0).strip()        
        if all(word.istitle() for word in first_line.split()):
            return first_line
        else:
            return None    

    words = first_line.split()
    extracted_name_list = extract_name_from_resume(resume_text)
    email = extract_email(resume_text)  # Ensure email is a string
    name  = confirm_name(words, extracted_name_list, email)  # Pass email correctly
    return name if len(name) <= 5 else None  # If too long, it's likely not a name

def get_personal_details(resume_text):
    personal_info = {
        'name': extract_name(resume_text),
        'email': extract_email(resume_text),
        'phone': extract_phone(resume_text),
    }
    return personal_info
