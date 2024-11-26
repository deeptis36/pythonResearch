import re
import pdfplumber

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Function to extract education
def extract_education(text):
    return extract_education_section(text)
    

# Main function
def parse_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    return text

def extract_education_section4(text):
    text_array = text.split("\n")
    start_capture = False
    section = []
    for line in text_array:
      if line=="EDUCATION":
        start_capture = True
    
      if start_capture:
        section.append(line)
        
    print(line)
    return None



def extract_education_section3(text):
    text_array = text.split("\n")
    start_capture = False
    section = []
    
    for line in text_array:
        # Start capturing when "EDUCATION" section begins
        if "EDUCATION" in line.upper():
            start_capture = True
            continue  # Skip the line with "EDUCATION" as it’s just the header
        
        # Stop capturing if another section starts
        if start_capture and (line.strip().isupper() and line.strip() not in ["", "EDUCATION"]):
            break
        
        # Capture the lines within the "EDUCATION" section
        if start_capture:
            section.append(line.strip())

    # Join the captured lines into a single string or return as list of lines
    education_text = "\n".join(section)
    return education_text


def extract_education_section2(text):
    text_array = text.split("\n")
    start_capture = False
    section = []
    
    # Keywords to identify the education section (case-insensitive)
    education_keywords = [
    "EDUCATION", "EDUCATIONS", "ACADEMIC DETAILS", "ACADEMY",
    "ACADEMICS", "QUALIFICATIONS", "QUALIFICATION", "ACADEMIC BACKGROUND",
    "EDUCATIONAL BACKGROUND", "EDUCATIONAL HISTORY", "SCHOOLING", "UNIVERSITY",
    "COLLEGE", "COURSEWORK", "STUDIES", "DEGREE", "DEGREES",
    "ACADEMIC QUALIFICATIONS", "ACADEMIC RECORD", "CREDENTIALS",
    "CERTIFICATIONS", "ACADEMIC ACHIEVEMENTS", "EDUCATION HISTORY",
    "EDUCATIONAL QUALIFICATIONS", "EDUCATIONAL PROFILE"
]
    
    for line in text_array:
        # Check if the line contains any of the keywords
        if any(keyword in line.upper() for keyword in education_keywords):
            start_capture = True
            continue  # Skip the line with the section header

        # Stop capturing if another section starts
        if start_capture and (line.strip().isupper() and line.strip() not in [""] + education_keywords):
            break

        # Capture the lines within the "EDUCATION" section
        if start_capture:
            section.append(line.strip())

    # Join the captured lines into a single string or return as list of lines
    education_text = "\n".join(section)
    return education_text

def extract_education_section(text):
    text_array = text.split("\n")
    start_capture = False
    section = []
    education_records = []
    
    # Keywords to identify the education section (case-insensitive)
    education_keywords = [
        "EDUCATION", "EDUCATIONS", "ACADEMIC DETAILS", "ACADEMY",
        "ACADEMICS", "QUALIFICATIONS", "QUALIFICATION", "ACADEMIC BACKGROUND",
        "EDUCATIONAL BACKGROUND", "EDUCATIONAL HISTORY", "SCHOOLING", "UNIVERSITY",
        "COLLEGE", "COURSEWORK", "STUDIES", "DEGREE", "DEGREES",
        "ACADEMIC QUALIFICATIONS", "ACADEMIC RECORD", "CREDENTIALS",
        "CERTIFICATIONS", "ACADEMIC ACHIEVEMENTS", "EDUCATION HISTORY",
        "EDUCATIONAL QUALIFICATIONS", "EDUCATIONAL PROFILE"
    ]
    
    # Keywords that indicate a different section is starting
    other_sections = [
        "EXPERIENCE", "EXPERIENCES", "WORK EXPERIENCE", "WORK EXPERIENCES",
        "PROFESSIONAL EXPERIENCE", "PROFESSIONAL EXPERIENCES", "PROJECTS","PROJECT",
    ]

    # Iterate through each line in the text array
    for line in text_array:
        # Check if the line contains any of the education keywords (case-insensitive)
        if any(keyword in line.upper() for keyword in education_keywords):
            start_capture = True

        # Check if the line contains any of the other section keywords to stop capturing
        if any(keyword in line.upper() for keyword in other_sections):
            if start_capture:
                break  # Stop capturing if we're in the education section and another section starts
            start_capture = False

        # Capture the line if we are in the education section
        if start_capture:
           
            section.append(line.strip())
            section.append("###")

    # Return the captured lines as a single string
    return section


# Example usage
# resume_path = 'files/resume.pdf'  # Specify the path to your resume file
# resume_text = parse_resume(resume_path)

# education_section = extract_education_section(resume_text)
# print(education_section)
