import pdfplumber
import docx
import re

# Helper function to extract text from PDF
def extract_text_from_pdf(file_path):
    print(f"Extracting text from: {file_path}")
    print("This may take a moment...")
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# Helper function to extract text from DOCX
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Function to parse sections of the resume
def parse_resume_sections(text):
    sections = {}
    
    # Define regular expressions for sections
    section_patterns = {
        "name": r"^\s*Name\s*:\s*(.*)",
        "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
        "phone": r"\b(?:\+?\d{1,3})?[-.\s]?\(?\d{2,3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b",
        "skills": r"Skills:\s*(.*)",
        "experience": r"(?:Work Experience|Professional Experience|Employment History):\s*(.*)",
        "education": r"(?:Education|Academic Background):\s*(.*)"
    }
    
    # Match patterns to extract each section
    for section, pattern in section_patterns.items():
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
        if match:  # Check if match is found
            print(section)
            print(match)
            print("======================================")
            sections[section] = "match.group(1).strip()"
        else:
            sections[section] = None  # Assign None if no match found
    
    return sections


# Main function to parse resume based on file type
def parse_resume(file_path, file_type='pdf'):
    if file_type == 'pdf':
        text = extract_text_from_pdf(file_path)
    elif file_type == 'docx':
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type. Use 'pdf' or 'docx'.")

    # Extracted text processing
    parsed_sections = parse_resume_sections(text)
    return parsed_sections

# Example usage
file_path = "resume.pdf"  # Change to your resume file path
file_type = "pdf"  # Change to "docx" if using a DOCX file
print(f"Parsing resume: {file_path}")

resume_data = parse_resume(file_path, file_type=file_type)

# Output parsed resume data
for section, content in resume_data.items():
    print(f"{section.capitalize()}: {content}")
