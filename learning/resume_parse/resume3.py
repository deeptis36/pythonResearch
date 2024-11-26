import spacy
from pyresparser import ResumeParser

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Specify the path to the resume file
resume_file_path = 'resume.pdf'  # Ensure the PDF is in the same directory as the script

# Use the ResumeParser with the nlp model
data = ResumeParser(resume_file_path, nlp=nlp).get_extracted_data()
print(data)
