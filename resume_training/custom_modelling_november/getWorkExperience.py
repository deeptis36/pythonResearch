import spacy
import re
from fuzzywuzzy import fuzz
from resumeText import get_resume_text  # Ensure this is your custom module
from data import skill_array, roles_array,resume_classification ,work_keywords # Import your data arrays
from difflib import get_close_matches
from dateRange import extract_date_ranges
from role import get_role
from employer import get_employer
# Load spaCy model
nlp = spacy.load("en_core_web_sm")

other_section = list(set(resume_classification) - set(work_keywords))



def extract_work_section(resume_text):

    resume_text = resume_text.lower()
    lines = resume_text.split("\n")
    start_reading = False
    work_text = ""
    for line in lines:
        
        line = line.strip()
        words = line.split()
       
        if(len(words) == 0):
            continue
       
        if any(keyword in line.lower() for keyword in work_keywords) and len(words) <=3:
          
            start_reading = True
        
        if start_reading and all(keyword not in line.lower() for keyword in other_section) and len(words) <= 3:
         
            start_reading = False

        #and len(words) <=15
        
        if start_reading :            
            work_text += line + "\n"
          

    
    work_text = clean_text(work_text)
    print(work_text)
    exit("uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
    return work_text

def clean_line_from_data(line, dataList):
    data = " ".join(dataList)
   
    dataArr = data.split()
    
    for date in dataArr:
        line = line.replace(date, "")
        
    line = line.replace("-", "")
    line = line.replace("–", "") 

    return line.strip()
   

def clean_text(text):
    lines = text.split("\n")  # Split text into lines

    data = []
    
    extracted_data  = []
    
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
            line = clean_line_from_data(line, data)


        role = get_role(line)
        
        if role:
            data.append(role)
            tmp_role = role
            # professional_summary.append({"role":role})
        line = clean_line_from_data(line, data)
        


        employer = get_employer(line)

        if len(employer) >0:
            data.append(employer)
            tmp_employer = employer
            # professional_summary.append({"employer": employer})
        
        
       
        if(tmp_role != "" and tmp_date != "" and tmp_employer != ""):
            professional_summary.append({"role":tmp_role, "date":tmp_date, "employer":tmp_employer})
            extracted_data.append(professional_summary)
            tmp_role = ""
            tmp_date = ""
            tmp_employer =""
    
    
    return extracted_data



def extract_work_experience(work_section_array):

    tmpDateArr = []
    tmpEmployerArr = []
    tmpRoleArr = []

    work_experience = []
    
   
    return work_section_array 


def get_professional_summary(resume_text):
    work_section = extract_work_section(resume_text)

    extracted_data = extract_work_experience(work_section)
   
    return extracted_data


