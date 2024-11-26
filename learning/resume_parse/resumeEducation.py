import docx2txt
import nltk
import re
import spacy
# Add the NLTK data path
nltk.data.path.append('/home/preeti/nltk_data')
nlp = spacy.load("en_core_web_sm")
# Download necessary resources
nltk.download('stopwords', download_dir='/home/preeti/nltk_data')
nltk.download('punkt', download_dir='/home/preeti/nltk_data')
nltk.download('averaged_perceptron_tagger', download_dir='/home/preeti/nltk_data')
nltk.download('maxent_ne_chunker', download_dir='/home/preeti/nltk_data')
nltk.download('words', download_dir='/home/preeti/nltk_data')

DEGREE_KEYWORDS = ["b.sc", "m.sc", "mca", "b.tech", "m.tech", "phd","bachelor"]
INSTITUTION_KEYWORDS = ["university", "institute", "college", "academy", "school"]
RESERVED_KEYWORDS = ["education", "qualification", "qualifications", "institution", "year"]

def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    return txt.replace('\t', ' ') if txt else None
def clean_token(token):
    # Keep only alphanumeric characters and convert to lower case
    return re.sub(r'[^a-zA-Z0-9]', '', token).lower()

def retrieve_education_details(rows):
    education_data = []
    
    start_capture = False  # Flag to start capturing once institution is found
    cleaned_degree_keywords = [re.sub(r'[^a-zA-Z0-9]', '', degree.lower()) for degree in DEGREE_KEYWORDS]
   
    for row in rows:
        # Split the row into tokens
        # tokens = re.split(r'[|,]', row)
        tokens = re.split(r'[|,;]\s*|\n', row) 
        degree = None
        institution = None
        year = None
        print("\n") 
        for token in tokens:
            # Clean the token
            cleaned_token = clean_token(token)
            token_lower = cleaned_token.lower().strip()
            
          
            # Check if this token contains an institution keyword
            if  token_lower in RESERVED_KEYWORDS:
                start_capture = True  # Start capturing tokens from here
                institution = token.strip()
            # If start_capture is True, look for degree, institution, or year in token
            if start_capture:
               
                # Check for degree
                if any(degree_keyword in token_lower for degree_keyword in cleaned_degree_keywords):
                    degree = token.strip()
                
                # Check for institution again in case it appears after degree
                if any(inst in token_lower for inst in INSTITUTION_KEYWORDS):
                    institution = token.strip()

                doc = nlp(token)
               
                for doc_token in doc:
                   
                    if doc_token.pos_ == 'NUM':                       
                        year = doc_token.text
                        print(doc_token.text, doc_token.pos_)
                 
                print(f"Degree: {degree}, Institution: {institution}, Year: {year}")
               
                # If all parts are found, add them to education_data and reset
                if degree and institution and year:
                    education_data.append([degree, institution, year])
                    degree, institution, year = None, None, None  # Reset for next entry
                    # start_capture = False  # Reset capture for next entry

    return education_data

def parse_education_details(text):
    education_data = []
    rows = text.split('\n')
    start_capture = False  # Flag to start capturing once institution is found
    cleaned_degree_keywords = [re.sub(r'[^a-zA-Z0-9]', '', degree.lower()) for degree in DEGREE_KEYWORDS]
   
    education_data = retrieve_education_details(rows)
    return education_data

if __name__ == '__main__':
    text = extract_text_from_docx('resume.docx')
    # education_information = extract_education(text)
    education_details = parse_education_details(text)
    # print(education_information)
    print("\nEducation Details:")
    print(education_details)
