import spacy
import re
import fitz 
# Load the spaCy model
nlp = spacy.load("en_core_web_sm")
import re

def extract_employer_experience(text):
    employers = []
    experiences = []
    
    # Process text with spaCy
    doc = nlp(text)
    
    # Extract companies/employers by finding named entities that are "ORG" (organization)
    for ent in doc.ents:
        print(ent.text, ent.label_)
        if ent.label_ == "ORG":
            employers.append(ent.text)
    
    # Regular expressions for work experience durations
    experience_pattern = re.compile(r"(\d+)\s+(years?|months?)")
    date_pattern = re.compile(r"((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4})")
    
    # Find all experience matches
    experiences.extend(experience_pattern.findall(text))
    date_ranges = date_pattern.findall(text)

    # Organize extracted information
    experience_info = {
        "employers": list(set(employers)),  # Unique employers
        "durations": experiences,  # Duration patterns found
        "date_ranges": [" - ".join(match) for match in date_ranges]  # Date ranges found
    }
    
    return experience_info

def pdf_to_text(filepath):
    text = ""
    with fitz.open(filepath) as pdf:
        for page_num in range(pdf.page_count):
            page = pdf[page_num]
            text += page.get_text()
    return text

# Load PDF text and extract info

resume_text = pdf_to_text("resume.pdf")
extracted_info = extract_employer_experience(resume_text)
print(extracted_info)

