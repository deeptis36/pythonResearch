import spacy
import re
from fuzzywuzzy import fuzz
from resumeText import get_resume_text  # Ensure this is your custom module
from data import skill_array, roles_array,resume_classification  # Import your data arrays
from difflib import get_close_matches
# Load spaCy model
nlp = spacy.load("en_core_web_sm")



def extract_education_section(resume_text):

    lines = resume_text.split('\n')
    start_reading = False
    education_text = ""
    for line in lines:
      
        if "education" in line.lower():
            start_reading = True
            
        if start_reading:
            education_text += line + "\n"
    
    return education_text


def extract_college_degree_year(resume_text):
    # The main pattern to extract college/university, degree, and year
    pattern = r"(?P<college>[A-Za-z\s&]+(?:University|College))[\s\S]*?(?P<degree>[\w\s\.,&-]+(?:\([\w\s]+\))?)\s*,?\s*(?P<year>\d{4})"
    
    # The list of patterns for various institutions
    patterns = [
        r"\b([A-Za-z\s]+University)\b",  # University
        r"\b([A-Za-z\s]+College)\b",     # College
        r"\b([A-Za-z\s]+Institute)\b",   # Institute
        r"\b([A-Za-z\s]+(College|University))\b",  # College or University
        r"\b([A-Za-z\s]+(University|College|Institute|School|Academy))\b",  # Comprehensive
        r"\b([A-Za-z\s]+(U|Inst\.|Col\.)?)\b",  # Abbreviated institutions
        r"\b([A-Za-z\s]+(University|College|Institute|Academy|School|U|Inst\.|Col\.)+)\b",  # Full with abbreviation
        r"\b([A-Za-z\s]+(Online|Virtual)\s(University|College|Institute))\b"  # Online/Virtual institutions
    ]
    
    # Store the results
    extracted_data = []

    # Iterate over each line in the resume
    lines = resume_text.split("\n")
    for line in lines:
        matches = []

        # Check if the line matches any of the patterns
        for pattern in patterns:
            # Use findall to capture all matches in the line
            matches.extend(re.findall(pattern, line))

        # If matches found, process them
        for match in matches:
            # Extract college and degree if matches are found
            college = match[0].strip()  # match[0] corresponds to the matched college name
            degree = match[1].strip() if len(match) > 1 else "Unknown Degree"
            
            # Look for year using the main pattern (we expect year to be in the line)
            year_match = re.search(r"\d{4}", line)
            year = year_match.group() if year_match else "Unknown Year"

            # Append the extracted data
            extracted_data.append({
                "college": college,
                # "degree": degree,
                # "year": year
            })

    # Return the extracted data
    return extracted_data


def extract_degree(line):
    # Predefined list of known degrees
    degrees = [
        "Associate of Arts (AA)", "Associate of Science (AS)", "Associate of Applied Science (AAS)",
        "Associate of Engineering (AE)", "Associate of Fine Arts (AFA)", "Bachelor of Arts (BA)",
        "Bachelor of Science (BS)", "Bachelor of Fine Arts (BFA)", "Bachelor of Business Administration (BBA)",
        "Bachelor of Engineering (BE)", "Bachelor of Technology (BTech)", "Bachelor of Architecture (BArch)",
        "Bachelor of Commerce (BCom)", "Bachelor of Laws (LLB)", "Bachelor of Medicine and Bachelor of Surgery (MBBS)",
        "Bachelor of Computer Science (BCS)", "Bachelor of Nursing (BSN)", "Master of Arts (MA)", "Master of Science (MS)",
        "Master of Business Administration (MBA)", "Master of Engineering (MEng)", "Master of Technology (MTech)",
        "Master of Fine Arts (MFA)", "Master of Laws (LLM)", "Master of Public Health (MPH)", "Master of Social Work (MSW)",
        "Master of Computer Applications (MCA)", "Doctor of Philosophy (PhD)", "Doctor of Science (DSc)", "Doctor of Engineering (DEng)",
        "Doctor of Business Administration (DBA)", "Doctor of Medicine (MD)", "Juris Doctor (JD)", "Doctor of Dental Surgery (DDS)",
        "Doctor of Pharmacy (PharmD)", "Doctor of Veterinary Medicine (DVM)", "Doctor of Education (EdD)", "Doctor of Osteopathic Medicine (DO)",    
        "Doctor of Public Health (DrPH)"
    ]
    
    words = line.split()
    
    for word in words:
        if word in degrees:
            return word


# File path to resume
file_path = "files/Resume_201124143407_JAY_MUZEIN.docx"
resume_text = get_resume_text(file_path)
if(resume_text == None):
    print("file not readable")
# Extract names
education_text = extract_education_section(resume_text)
extracted_data = extract_college_degree_year(education_text)
print(extracted_data)
