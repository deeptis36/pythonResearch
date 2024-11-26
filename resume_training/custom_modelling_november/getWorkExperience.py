import spacy
import re
from fuzzywuzzy import fuzz
from resumeText import get_resume_text  # Ensure this is your custom module
from data import skill_array, roles_array,resume_classification ,work_keywords # Import your data arrays
from difflib import get_close_matches
# Load spaCy model
nlp = spacy.load("en_core_web_sm")

other_section = list(set(resume_classification) - set(work_keywords))

def extract_work_section(resume_text):

    lines = resume_text.split("\n")
    start_reading = False
    work_text = ""
    for line in lines:
        line = line.strip()
        if any(keyword in line.lower() for keyword in work_keywords):
            start_reading = True
        
        if any(keyword in line.lower() for keyword in other_section):
            start_reading = False

        if start_reading:
            print(line)
            work_text += line + "\n"
  
    return work_text


# File path to resume
file_path = "files/Resume_201124143407_JAY_MUZEIN.docx"
resume_text = get_resume_text(file_path)
if(resume_text == None):
    print("file not readable")



work_section = extract_work_section(resume_text)

# print(work_section)
# Extract names

