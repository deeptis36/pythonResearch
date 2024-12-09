import spacy
import re
from fuzzywuzzy import fuzz
from resumeText import get_resume_text  # Ensure this is your custom module
from data import skill_array, month_array,resume_classification ,work_keywords,roles_array # Import your data arrays
from difflib import get_close_matches
from dateRange import extract_date_ranges
from role import get_role
from employer import get_employer
# Load spaCy model
nlp = spacy.load("en_core_web_sm")

other_section = list(set(resume_classification) - set(work_keywords))

reservers_keywords = skill_array + month_array + resume_classification + work_keywords+roles_array
skip_to_ignore = ["role:", "designation:", "worked as:", "role: ", "worked as: "]
MAX_LENGTH = 12
def check_for_text_to_ignore(text):
   
    clean_text = re.sub(r'[^\w\s,.]', ' ', text)  # Remove special chars except commas and spaces
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()  # Normalize spaces
    # print("\n__________________________________________________________\n")
    # print(f"TEXT: {text}")
    word_count = word_in_text(text)
  
    if word_count == 0:
        return True
    
    doc = nlp(clean_text)
    
    for ent in doc.ents:
        
        if ent.label_ in {"DATE"}:
            return False
   
    if text.strip() in reservers_keywords:
        return False
    
    for token in doc:
        if token.text == "professional":
            return False
        if token.text.strip() in reservers_keywords:
            return False
        if( token.pos_ == "ADP" or token.pos_ == "ADJ" or token.pos_ == "AUX" or token.pos_ == "DET" or token.pos_ == "ADV" ):
            # print(f"TOKEN: {token.text} - POS: {token.pos_}")
            return True
        if token.pos_ == "VERB" and token.text.lower() not in month_array and token.text.lower() not in reservers_keywords and token.text.lower() not in skip_to_ignore:
            # print(f"TOKEN: {token.text} - POS: {token.pos_}")
            return True
    

    if word_count > MAX_LENGTH:
        
        return True
    
    
    return False



def extract_work_section(resume_text):

    resume_text = resume_text.lower()
    lines = resume_text.split("\n")
    start_reading = False
    work_text = ""
    for line in lines:
     
       
        line_to_add = line
        clean_text = re.sub(r'[^\w\s,.]', ' ', line)  # Remove special chars except commas and spaces
        # clean_text = re.sub(r'\.', '', clean_text)   # Remove periods
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()  
        line = clean_text.strip()
    
        if  check_for_text_to_ignore(line):
          
            continue

        
        
        word_count = word_in_text(line)

        # print(line,"\n")
       
        if line.lower() in work_keywords or any(keyword in line.lower() for keyword in work_keywords) and word_count <=3:
            # print(f"start reading: {line}")         
            start_reading = True

        if start_reading  and word_count <=3:
            word = line.split()[0]
            if word in other_section:
                # print(f"stop reading: {line}")
                start_reading = False
                
        
        if start_reading :
           
            work_text += line_to_add + "\n"

    print(work_text)
    # exit("ggggggggggggggggggggggggggg")
    # work_text = clean_resume_text(work_text)
    
   
    return work_text

def clean_line_from_data(line, needles):
  
  

    # Remove each needle from the line
    for needle in needles:
       needle_split = needle.split()
       for word in needle_split:          
           line = line.replace(word, "")
    line = line.replace("-", "")
    line = line.replace("–", "")
    # line = line.replace("|", "")
    
    
    return line.strip(), ""
    
   

def clean_resume_text(text):
    lines = text.split("\n")  # Split text into lines

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
            data.append("to")
            data.append("-")
            
            tmp_date_array.append(tmp_date)

        line,data1 = clean_line_from_data(line, data)
       
        role = get_role(line)
      

        if role:
           
            data.append(role)
            tmp_role = role
           
            tmp_role_array.append(role)
      
        line , data1 = clean_line_from_data(line, data)
        employer = get_employer(line)
        
        if len(employer) >0:
            data.append(employer)
            tmp_employer = employer
            tmp_employer_array.append(employer)
       

        if(tmp_role != "" and tmp_date != "" and tmp_employer != ""):           
            professional_summary.append({"role":tmp_role, "date":tmp_date, "employer":tmp_employer})            
            extracted_data.append(professional_summary)
            tmp_role = ""
            tmp_date = ""
            tmp_employer =""
            data = []
    
      


    # print(extracted_data)
    # print()

    # print("ROLE")
    # print(tmp_role_array)
    # print()
    # print("Date")
    # print(tmp_date_array)
    # print()
    
    # print("EMPLOYER")
    # print(tmp_employer_array)

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


folder = "files"
file = "Resume_201124145201_.docx"
file  = folder+"/"+file

resume_text = get_resume_text(file)


professional_summary = get_professional_summary(resume_text)
# print(professional_summary)
