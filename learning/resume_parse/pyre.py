import fitz  # PyMuPDF

# Import PyReParse
from pyreparse import PyReParse as PRP

# Define callback function for a specific pattern
def on_pattern_001(prp_instance, pat_name):
    if pat_name != 'pattern_001':
        print(f'Got wrong pattern name [{pat_name}].')

# Define Regular Expression Patterns Data Structure
regexp_pats = {
    'pattern_001': {
        're_string': r'^Test\s+Pattern\s+(?P<pat_val>\d+)',  # Regex pattern as a string
        'field_name': 'value',                               # Field name for the matched value as a string
        'callback': on_pattern_001,                          # Callback function for this pattern
        'trigger_on': 'True',                                 # Ensure this is a string
        'trigger_off': 'True'                                # Add trigger_off key
    },
    # Add more patterns as needed
}

# Create an Instance of PyReParse
prp = PRP(regexp_pats)

# Define the input file path
file_path = 'resume.pdf'  # Replace with your actual file path

# Open the PDF file using PyMuPDF
doc = fitz.open(file_path)

# Extract text from all pages of the PDF
pdf_text = ""
for page_num in range(doc.page_count):
    page = doc.load_page(page_num)
    pdf_text += page.get_text()

# Now process the extracted text line by line
for line in pdf_text.splitlines():
    # Call prp.match(line) to process the line against the defined patterns
    print(line)
    match_def, matched_fields = prp.match(line)
    # print( match_def, matched_fields)
    # # Check if any matches were found and process the results
    # if match_def:
    #     print(f"Matched Pattern: {match_def}")
    #     print(f"Matched Fields: {matched_fields}")
    # else:
    #     print("No match found.")
