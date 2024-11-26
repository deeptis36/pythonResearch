import re
import pdfplumber
import spacy
from datetime import datetime
from dateutil import parser
from experienceDates import extract_dates
# Load the English model
nlp = spacy.load("en_core_web_sm")

delim = "######"
# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"  # Add newline to separate pages
    return text




# Function to extract the professional experience section
def extract_professional_experience_section(text):
    

    text_array = text.split("\n")
    start_capture = False
    section = []
    # Keywords to identify the professional experience section (case-insensitive)
    experience_keywords = [
        "PROFESSIONAL EXPERIENCE", "WORK EXPERIENCE", "EXPERIENCE", "EMPLOYMENT HISTORY",
        "CAREER HISTORY", "PROFESSIONAL HISTORY", "WORK HISTORY", "EMPLOYMENT", "CAREER",
        "JOB EXPERIENCE", "PROFESSIONAL BACKGROUND", "WORK SUMMARY",
        "WORK TIMELINE", "WORK EXPERIENCE SUMMARY", "OCCUPATIONAL EXPERIENCE", 
        
    ]

    
    # Keywords indicating the end of a professional experience section
    other_sections = [
        "EDUCATION", "QUALIFICATIONS", "CERTIFICATIONS", "SKILLS", "PROJECTS", 
         "INTERNSHIP", "INTERNSHIPS", "TRAINING", "LANGUAGES",
        "EDUCATIONS", "ACADEMIC DETAILS", "ACADEMY",
        "ACADEMICS", "QUALIFICATIONS", "QUALIFICATION", "ACADEMIC BACKGROUND",
        "EDUCATIONAL BACKGROUND", "EDUCATIONAL HISTORY", "SCHOOLING", "UNIVERSITY",
        "COLLEGE", "COURSEWORK", "STUDIES", "DEGREE", "DEGREES",
        "ACADEMIC QUALIFICATIONS", "ACADEMIC RECORD", "CREDENTIALS",
        "CERTIFICATIONS", "ACADEMIC ACHIEVEMENTS", "EDUCATION HISTORY",
        "EDUCATIONAL QUALIFICATIONS", "EDUCATIONAL PROFILE","SUMMARY",
    ]

    # Iterate through each line in the text array
    for line in text_array:
        # Start capturing if the line contains any professional experience keywords
        if any(keyword in line.upper() for keyword in experience_keywords):
            start_capture = True
           

        # Stop capturing if any other section starts
        if start_capture and any(keyword in line.upper() for keyword  in other_sections):
            start_capture = False

        # Capture the line if within the professional experience section
        if start_capture:
            section.append(line.strip()+delim)

    # Join the captured lines into a single string for easier reading
    experience_text = "\n".join(section)
    return experience_text



def extract_professional_history(text):
    professiona_text = extract_professional_experience_section(text)
    return extract_job_roles(professiona_text)



# Load the spaCy model

def extract_job_roles(text):
    """
    Extracts job roles and employers from the given text.
    
    Parameters:
        text (str): The text containing job roles and employers.
        
    Returns:
        dict: A dictionary containing 'job_roles' and 'employers'.
    """
    # Initialize the lists
    job_roles = []
    employers = []
    experience_dates = []
    # Process the entire text with spaCy
    textArray = text.split(delim)
    for text in textArray:
        doc = nlp(text)
        # print(text)
        dates = extract_dates(text)
       
        if dates:
            experience_dates.append(dates)
        # Iterate over the tokens to extract job roles and employers
        extract_organizations(text)
        # Iterate over the tokens to extract job roles and employers
        # for token in doc:
        #     print(token)
    # print(experience_dates)
    return {'job_roles': job_roles, 'employers': employers, 'experience_dates': experience_dates}



def extract_job_roles_and_employers1(text):
    """
    Extracts job roles and employers from the given text, handling variable delimiters.
    
    Parameters:
        text (str): The text containing job roles and employer information.
        
    Returns:
        list of tuples: Each tuple contains a job role and an employer/organization name.
    """
    # Regular expression pattern to find job roles and associated employers
    # Using flexible delimiters: space, comma, or pipe
    pattern = r"([A-Z][a-z]*(?:\s[A-Za-z]*)*\s(?:Engineer|Developer|Manager|Assistant project manager|Software Engineer|Web Developer))\s*[,\|]?\s*([A-Za-z\s]+(?: Pvt\. Ltd\.| Solutions| Services| Institute| Technologies| Corporation)?)"

    # Find all job roles and employers with flexible delimiters
    job_roles_and_employers = re.findall(pattern, text)
    
    return job_roles_and_employers


def extract_job_roles_and_employers(text):
    """
    Extracts job roles and employers from the given text using modular pattern arrays.
    
    Parameters:
        text (str): The text containing job roles and employer information.
        
    Returns:
        list of tuples: Each tuple contains a job role and an employer/organization name.
    """
    # Define arrays for job titles and employer keywords
    job_titles = [
    "Engineer", "Software Engineer", "Sr. Software Engineer", "Junior Software Engineer", 
    "Developer", "Web Developer", "Backend Developer", "Frontend Developer", "Full Stack Developer", 
    "Manager", "Project Manager", "Product Manager", "Assistant Project Manager", "Marketing Manager", 
    "Operations Manager", "Sales Manager", "Business Development Manager", "Finance Manager", 
    "Account Manager", "Data Scientist", "Data Engineer", "Data Analyst", "Machine Learning Engineer", 
    "AI Engineer", "Designer", "Graphic Designer", "UI Designer", "UX Designer", "UX Researcher", 
    "Product Designer", "Creative Designer", "Art Director", "Content Strategist", "Content Manager", 
    "Content Writer", "Technical Writer", "Copywriter", "Business Analyst", "System Analyst", 
    "Quality Assurance Engineer", "QA Engineer", "QA Analyst", "Test Engineer", "Automation Engineer", 
    "IT Specialist", "Network Engineer", "Cloud Engineer", "DevOps Engineer", "Cybersecurity Analyst", 
    "Security Engineer", "Database Administrator", "Research Scientist", "Research Assistant", 
    "Accountant", "Financial Analyst", "Investment Analyst", "HR Manager", "HR Specialist", 
    "Recruiter", "Talent Acquisition Specialist", "Customer Service Representative", "Customer Support", 
    "Consultant", "Management Consultant", "Strategy Consultant", "Legal Advisor", "Legal Consultant", 
    "Compliance Officer", "Logistics Manager", "Supply Chain Manager", "Operations Analyst", 
    "Administrative Assistant", "Executive Assistant", "Office Manager", "Event Manager", 
    "Digital Marketing Specialist", "SEO Specialist", "Social Media Manager", "Campaign Manager", 
    "E-commerce Manager", "Product Owner", "Scrum Master", "Agile Coach", "Biomedical Engineer", 
    "Health Informatics Specialist", "Clinical Data Analyst", "Lab Technician", "Pharmacist", 
    "Nurse", "Doctor", "Surgeon", "Psychologist", "Physiotherapist", "Therapist"
]
    employer_keywords = ["Pvt\\. Ltd\\.", "Solutions", "Services", "Institute", "Technologies", "Corporation"]

    # Convert arrays to regex patterns
    job_titles_pattern = r"|".join(job_titles)  # Combines job titles with 'OR' logic
    employer_keywords_pattern = r"|".join(employer_keywords)  # Combines employer keywords with 'OR' logic

    # Regex pattern for job roles and employers
    pattern = rf"([A-Z][a-z]*(?:\s[A-Za-z]*)*\s(?:{job_titles_pattern}))\s*[,\|]?\s*([A-Za-z\s]+(?: {employer_keywords_pattern})?)"

    # Find all job roles and employers
    job_roles_and_employers = re.findall(pattern, text)
    
    return job_roles_and_employers


def extract_organizations(text):
    # Process text with spaCy model
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    # Extract entities labeled as ORG (organizations)
    organizations = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    
    # Remove duplicates by converting to a set and back to list
    organizations = list(set(organizations))
    # print(organizations)

    # Print extracted organizations
    # for org_text in organizations:
    #     org_doc = nlp(org_text)  # Process each organization name individually
    #     pos_tags = [(token.text, token,token.pos_) for token in org_doc]  # List of (word, POS) tuples
        
    #     print("Extracted Organization:", org_text)
    #     print("POS Tags:", pos_tags)
    #     print()  # For
    return organizations





# Main function to parse resume and extract professional experience section
def parse_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    experience_section = extract_professional_experience_section(text)
    return experience_section

# # Example usage
# resume_path = 'files/resume.pdf'  # Specify the path to your resume file
# professional_experience_section = parse_resume(resume_path)
# job_roles = extract_job_roles(professional_experience_section)
# employers = extract_job_roles_and_employers(professional_experience_section)
# # print(employers)
# # print(professional_experience_section)
# # print(job_roles)
