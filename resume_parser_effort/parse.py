import os
import re
from personalDetail import get_personal_details
from resumeText import get_resume_text
from education import extract_education
from professionalHistory import extract_professional_history
# from resume_parser import resumeparse
from skill import extract_skills
# Define the path to the folder containing the resume files
folder_path = "files/"



# Loop through each file in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a specific DOCX file
    if True: #filename == "Resume_051124151809_.pdf":
        print(f"{filename}:")
        # Build the full file path
        docx_path = os.path.join(folder_path, filename)
        

       
        # Extract personal details from the resume DOCX
        resume_text = get_resume_text(docx_path)
       
       
        if resume_text is not None:
            personal_info = get_personal_details(resume_text)
            print(personal_info)
            
            # education_details = extract_education(resume_text)
            # skill = extract_skills(resume_text)
            professional_details = extract_professional_history(resume_text)
           
          
            print(professional_details)
            print("\n" + "*"*50 + "\n")
           