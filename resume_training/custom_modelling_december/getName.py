import spacy
import re
from fuzzywuzzy import fuzz
from resumeText import get_resume_text  # Ensure this is your custom module
from data import skill_array, roles_array,resume_classification  # Import your data arrays
from difflib import get_close_matches
# Load spaCy model
nlp = spacy.load("en_core_web_sm")

ignore_array = skill_array+roles_array
def extract_personal_info(text):
   
    text  = text.lower()
    resume_keywords = [keyword.lower() for keyword in resume_classification]  
    personal_info =""
    resume_text_arr = text.split("\n")
    isfound = False
    for line in resume_text_arr:
        # Check if the line contains any of the keywords
        if any(keyword in line for keyword in resume_keywords):
            break  # Stop if a keyword is found
        else:
            personal_info += line + "\n"  # 
    
    return personal_info.strip()
   

def clear_text(text):
    """
    Clean and preprocess the text by removing unnecessary patterns.
    """
    text = text.strip()
    text = re.sub(r'Name\s*:', ' ', text, flags=re.IGNORECASE)  # Handle "Name:" or "Name :" case-insensitively
    return text


def extract_email(text):
    """
    Extract email addresses from the text using regex.
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails

def get_name_with_name_tag(extract_personal_info_array):
      for line in extract_personal_info_array:
        if "name" in line:
            name = line.split("name:")[1].strip()
            return name

def clearLine(line):
    # Define patterns to detect
    patterns = [
        r"phone:",       # Matches "phone:"
        r"ph:",          # Matches "ph:"
        r"email:",       # Matches "email:"
        r"emailID:",
        r"\n",
        r"\t" ,
        r"objective",","
        
    ]
    
    # Combine patterns into a single regex
    combined_pattern = r"|".join(patterns)
    
    # Split the text on the combined pattern
    result = re.split(combined_pattern, line, flags=re.IGNORECASE)[0]
    result =result.split("|")[0]
    
    # Return cleaned text after stripping extra whitespace
    return result.strip()

def extract_name_from_text(extract_personal_info_array):
   
    """
    Extracts the first probable name from the given array of text lines.
    Args:
        extract_personal_info_array (list): List of strings representing lines of text.
    Returns:
        str: Extracted name or "No name found".
    """
    # Define the regex pattern for matching names
    # name_pattern = r'^[A-Za-z ]+$'  # Matches lines with only alphabetic characters and spaces
    name_pattern = r"^[A-Za-z. ]+$"
    threshold = 80
    if_ignore = False
    for line in extract_personal_info_array:
        
        words = line.split()
        for word in words:         
            if word in ignore_array:
                if_ignore = True          
                break
       
        if if_ignore:
           if_ignore = False
           continue

     
        
        # Check if the line matches the name pattern
        line = clearLine(line)
        
        if re.match(name_pattern, line) and len(line.split()) >= 1:  # Assuming names have at least two words
            return line
    return "No name found"




def get_name(text):

    extracted_info = extract_personal_info(text)    
    extract_personal_info_array = extracted_info.split("\n")
    
  
    if "name" in extracted_info:
        name = get_name_with_name_tag(extract_personal_info_array)
        return name
    else:
        name = extract_name_from_text(extract_personal_info_array)
        return name
    


# File path to resume
# file_path = "files/Resume_201124143407_JAY_MUZEIN.docx"
# resume_text = get_resume_text(file_path)
# if(resume_text == None):
#     print("file not readable")
# # Extract names
# names = get_name(resume_text)
# print("Extracted Names:", names)
