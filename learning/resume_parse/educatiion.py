import re
import spacy
import pdfplumber

# Load spaCy model for tokenization and POS tagging
nlp = spacy.load("en_core_web_sm")

def clean_token(token):
    """Clean tokens by removing non-alphanumeric characters and extra spaces."""
    return re.sub(r'[^a-zA-Z0-9\s]', '', token).strip()

def extract_year_from_token(token):
    """Extract the year from a given token using spaCy for better accuracy."""
    doc = nlp(token)
    for doc_token in doc:
        if doc_token.pos_ == 'NUM':  # Looking for numbers (years)
            return doc_token.text
    return None

def retrieve_education_details(text):
    """Extract education details like degree, institution, and year from resume text."""
    education_data = []

    # Define regex patterns for degree, institution, and year
    degree_pattern = r'\b(B\.?Sc\.?|M\.?Sc\.?|M\.?C\.?A\.?|B\.?Tech\.?|M\.?Tech\.?|Ph\.?D|Bachelor\'s?|Master\'s?|Diploma)\b'
    institution_pattern = r'\b(?:University|Institute|College|Academy|School|College|Academy|Department)\b'
    year_pattern = r'\b(19|20)\d{2}\b'

    # Split the input text into lines or sentences (you may adjust this based on input format)
    rows = text.split('\n')

    for row in rows:
        tokens = re.split(r'[|,;]\s*|\n', row)
        
        degree, institution, year = None, None, None

        # Process each token in the row
        for token in tokens:
            cleaned_token = clean_token(token)
            
            # Match degree (degree pattern)
            if re.search(degree_pattern, cleaned_token, re.IGNORECASE):
                degree = token.strip()
            
            # Match institution (institution pattern)
            if re.search(institution_pattern, cleaned_token, re.IGNORECASE):
                institution = token.strip()
            
            # Extract year using regex
            if re.search(year_pattern, cleaned_token):
                year = extract_year_from_token(token)

            # If all components are found, add to result and break
            if degree and institution and year:
                education_data.append([degree, institution, year])
                break  # Exit loop once a valid entry is found

    return education_data
def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using pdfplumber."""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            # Iterate over all pages in the PDF
            for page in pdf.pages:
                # Extract text from each page
                text += page.extract_text()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
    return text
# Sample resume text (as it might appear in a .txt file)
resume_text = """
John Doe
Experience: Software Developer at ABC Corp (2018-2022)
Education:
B.Tech in Computer Science, XYZ University, 2019
M.Sc. in Physics, ABC Institute, 2021
Bachelor's in Civil Engineering, PQR College, 2017
"""
pdf_path = "resume.pdf"

# Extract text from the PDF
resume_text = extract_text_from_pdf(pdf_path)
# Extract education details from the resume text
education_details = retrieve_education_details(resume_text)

# Print the extracted education details
print("\nEducation Details:")
for detail in education_details:
    print(detail)
