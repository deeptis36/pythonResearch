import fitz  # PyMuPDF
import re

# Define regular expression patterns for common personal details
personal_details_patterns = {
    'name': r'([A-Z][a-z]+(?: [A-Z][a-z]+)+)',  # Match capitalized names with first and last names
    'email': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',  # Match email addresses
    'phone': r'(\+?\d{1,4}[\s\-]?)?(\(?\d{1,4}\)?[\s\-]?)?\d{7,10}',  # Match phone numbers (international format)
    # 'address': r'\d{1,5}\s(?:[A-Za-z0-9#.,/]+(?:\s[A-Za-z0-9#.,/]+)*)(?:,\s[A-Za-z]+){1,3}',  # Match address
}

# Open the PDF file using PyMuPDF
file_path = 'pragati resume.pdf'  # Replace with your actual file path
doc = fitz.open(file_path)

# Extract text from all pages of the PDF
pdf_text = ""
for page_num in range(doc.page_count):
    page = doc.load_page(page_num)
    pdf_text += page.get_text()

# Function to extract details using regex patterns
def extract_personal_details(text, patterns):
    extracted_details = {}
    
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            extracted_details[key] = match.group(0)
        else:
            extracted_details[key] = "Not Found"
    
    return extracted_details

# Extract personal details from the PDF text
personal_details = extract_personal_details(pdf_text, personal_details_patterns)

# Print the extracted personal details
print("Extracted Personal Details:")
for key, value in personal_details.items():
    print(f"{key.capitalize()}: {value}")
