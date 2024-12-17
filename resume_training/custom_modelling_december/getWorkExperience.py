import spacy
import re
from fuzzywuzzy import fuzz
from resumeText import get_resume_text  # Ensure this is your custom module
from data import skill_array,degrees, month_array,resume_classification ,work_keywords,roles_array # Import your data arrays
from difflib import get_close_matches
from dateRange import extract_date_ranges
from role import get_role
from employer import get_employer
# Load spaCy model
nlp = spacy.load("en_core_web_sm")

other_section = list(set(resume_classification) - set(work_keywords))

reservers_keywords =  month_array + resume_classification + work_keywords+roles_array
skip_to_ignore = ["role:", "designation:", "worked as:", "role: ", "worked as: "]
MAX_LENGTH = 12



def find_matches_in_text(text, keyword_arrays):
    """
    Check if the text contains any keywords from the given arrays.
    
    Args:
        text (str): The input text to search.
        keyword_arrays (list): A list of arrays, where each array contains keywords to match.
    
    Returns:
        list: A list of matched keywords. If no matches are found, returns an empty list.
    """
    # Combine all keywords into one list
    # combined_keywords = []
    # for array in keyword_arrays:
    #     combined_keywords.extend(array)
    
    # Create a regex pattern from the combined keywords
    pattern = "|".join(map(re.escape, keyword_arrays))
    
    # Find all matches in the text
    matches = re.findall(pattern, text, re.IGNORECASE)  # Case-insensitive match
    
    return matches
def check_for_text_to_ignore(text):
   
    clean_text = re.sub(r'[^\w\s,.]', ' ', text)  # Remove special chars except commas and spaces
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()  # Normalize spaces
    
    word_count = word_in_text(text)
  
    if word_count == 0:
        return True
    if word_count > MAX_LENGTH:
        
        return True
    
    doc = nlp(clean_text)
    
    reserve_matches = find_matches_in_text(text.strip() , reservers_keywords)
    if len(reserve_matches) > 0:
        return False
    
    for ent in doc.ents:
        if ent.label_ in degrees:
            return True
        
        if ent.label_ in {"DATE"}:
            return False
   
    if text.strip() in reservers_keywords:
        return False
    
    for ent in doc.ents:
        
        if ent.label_ in {"ORG", "GPE"}:
            return False

    for token in doc:
        if token.text == "professional":
          
            return False
        if token.text.strip() in reservers_keywords:
            return False
        if( token.pos_ in {"ADP", "ADJ", "AUX", "DET", "ADV"} ):
            return True
        if token.pos_ == "VERB" and token.text.lower() not in month_array and token.text.lower() not in reservers_keywords and token.text.lower() not in skip_to_ignore:
         
            return True
    
    return False



def extract_work_section(resume_text):

    resume_text = resume_text.lower()
    newlines = resume_text.split("\n")
    start_reading = False
    work_text = ""
    
    filtered_lines = [line for line in newlines if not line.lower().startswith("experience in")]
    filtered_lines = [line for line in filtered_lines if not line.lower().startswith("familiarity with")]
    filtered_lines = [line for line in filtered_lines if not line.lower().startswith("responsible for")]
    filtered_lines = [line for line in filtered_lines if not line.lower().startswith("experience with")]
    
    
    
    for tab_line in filtered_lines:
        lines = tab_line.split("\t")
    
        for line in lines:
            
        
        
            line_to_add = line
            clean_text = re.sub(r'[^\w\s,.]', ' ', line)  # Remove special chars except commas and spaces
            # clean_text = re.sub(r'\.', '', clean_text)   # Remove periods
            clean_text = re.sub(r'\s+', ' ', clean_text).strip()  
            line = clean_text.strip()
        
            if  check_for_text_to_ignore(line):
            
                continue

            
            
            word_count = word_in_text(line)

            
            if line.lower() in work_keywords or any(keyword in line.lower() for keyword in work_keywords) and word_count <=3:
                    
                start_reading = True

            if start_reading  and word_count <=3:
                word = line.split()[0]
                if word in other_section:
                    start_reading = False
                    
            
            if start_reading :
            
                work_text += line_to_add + "\n"

    
    work_text = clean_resume_text(work_text)
   
    return work_text

def clean_line_from_data(line, needles):
    """
    Cleans a line by removing all words found in the needles list.

    Args:
        line (str): The input string to be cleaned.
        needles (list): A list of strings (needles) to remove from the line.

    Returns:
        str: The cleaned string.
    """
    if not isinstance(line, str) or not isinstance(needles, list):
        raise ValueError("Invalid input: 'line' must be a string and 'needles' must be a list.")
    
 
    
    for needle in needles:
            if isinstance(needle, str):
                for word in needle.split():  # Split the needle into words
                    word = word.strip()
                    if word:  # Avoid empty strings
                        # Use word boundaries (\b) to replace only whole words
                        line = re.sub(rf'\b{re.escape(word)}\b', '', line)

    # Replace additional unwanted characters
    unwanted_chars = ["-", "–", "|"]
    for char in unwanted_chars:
        line = line.replace(char, "")

    # Return the stripped and cleaned line
    return line.strip()


def clean_resume_text(text):
    lines = text.split("\n") 
    data = []
    
    extracted_data  = []
    

    tmp_role_array = []
    tmp_date_array = []
    tmp_employer_array = []

    index = 0
    tmp_role = ""
    tmp_date = ""
    tmp_employer =""
    for line in lines:
       
        words = line.split()
        word_count = len(words)
        
        if line in resume_classification:
            continue
       
        line = line.strip()
        professional_summary = []
        date_range = extract_date_ranges(line)

        if len(date_range) >0:           
            tmp_date = date_range[0]
            data.append(date_range[0])
            # data.append("to")
            data.append("-")
            
            tmp_date_array.append(tmp_date)
      
       
        line = clean_line_from_data(line, data)
       
        role = get_role(line)

        if role:
                
            data.append(role)
            tmp_role = role
           
            tmp_role_array.append(role)
      
        line = clean_line_from_data(line, data)
        if tmp_employer == "":
            employer = get_employer(line)
        
        if len(employer) >0:
            data.append(employer)
            tmp_employer = employer
            tmp_employer_array.append(employer)
        # print(f"{tmp_role} - {tmp_date} - {tmp_employer}\n")

        if(tmp_role != "" and tmp_date != "" and tmp_employer != ""):
            # print("EMPLOYER")
            # print(f"{tmp_role} - {tmp_date} - {tmp_employer}\n")        
            professional_summary.append({"role":tmp_role, "date":tmp_date, "employer":tmp_employer})            
            extracted_data.append(professional_summary)
            tmp_role = ""
            tmp_date = ""
            tmp_employer =""
            data = []
    
      



    return extracted_data


def word_in_text(text):
    word_count =0
    for word in text.split():
        if len(word.strip()) > 0:
            word_count += 1
    
    return word_count

def extract_work_experience(work_section_array):

    """
    Extract work experience from the resume text.
    this method is done for future reference
    """
    tmpDateArr = []
    tmpEmployerArr = []
    tmpRoleArr = []

    work_experience = []
    
   
    return work_section_array 


def get_professional_summary(resume_text):
    
    work_section = extract_work_section(resume_text)
   
   
    extracted_data = extract_work_experience(work_section)
   
    return extracted_data


# folder = "files"
# file = "Resume_091224134153_.docx"
# file  = folder+"/"+file

# resume_text = get_resume_text(file)

# professional_summary = get_professional_summary(resume_text)
