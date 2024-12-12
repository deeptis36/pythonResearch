import spacy
import os
import traceback
import json
from datetime import datetime
from resumeText import get_resume_text,get_text_or_delete_if_not_readable
from GeneratePositioning import get_word_positions,get_skills,get_name_entity,get_phone_entity,get_professional
from employer import get_employer
# Generate a timestamped output file name
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"json/output_{current_datetime}.json"

# Ensure the 'json' directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Initialize a counter for processed records
processed_count = 0
folder_path = "resumesets"
folder_path = "files"

# Array to hold extracted resume data
resume_text_array = []

successfull_count = 0
failed_count = 0
# Process each file in the folder
for filename in os.listdir(folder_path):
    # Construct full file path
    file_path = os.path.join(folder_path, filename)
    
    file_name_array = []
    # Check if the file is a resume (optional filter by file extension)
    if filename.endswith((".pdf", ".doc", ".docx")):  # Adjust as needed
      
        
        # Extract text from the resume file
        try:
          
            entities = []

            entities.append({"resume": filename})
            #name
            
            terminating_file_name = "Gokul_CV_1124_1.docx"
            # terminating_file_name = "Resume_201124135354_Resuem-Savitha_Gadam.docx"
            terminating_file_name = "Deepti_resume03122024.docx"
            terminating_file_name = "Resume_201124141649_.docx"
            terminating_file_name = "Resume_201124152128_Patrick_Murphy_Resume_03.06.24_(1).pdf"
            terminating_file_name = "Resume_201124140703_.docx"
            if True and filename == terminating_file_name:
               
                print(f"\n***************************Processing File: {filename} *************************************")
        
                resume_text = get_resume_text(file_path)
                if(resume_text == None):
                    print("file not readable")
                    resume_text = get_text_or_delete_if_not_readable(file_path)
                    if resume_text == None:
                        continue

                entity_dict = get_word_positions(resume_text)
               
                entity_skill = get_skills(entity_dict)
               
                enitity_name = get_name_entity(resume_text)
                entity_phone = get_phone_entity(resume_text)
                
                email_entity = entity_dict.get("EMAIL")
                
                professional_entity = get_professional(resume_text)
                exit("aaaaa")
          
                
                exit("00000000000000000000000000000000000")

                if len(professional_entity) > 0 and  len(entity_phone) > 0 and email_entity and len(entity_skill) > 0:
                    successfull_count += 1
                    file_name_array.append(file_path)
                    
                    entities.append(enitity_name)

                   
                    for phone in entity_phone:                        
                        entities.append(phone)

                    email = email_entity[0]                 
                    entities.append(email)
                    
                    for skill in entity_skill:
                        entities.append(skill)
                    
                    entities.append(professional_entity)
                    # print(entities)
                    resume_data = {
                        "resume_text": resume_text,
                        "entities": entities,  # Adjust this to store parsed entities if needed
                    }
                    resume_text_array.append(resume_data)
                else:
                    failed_count += 1
                
                print("="*150)
                # exit(0)
           
                      
            processed_count += 1
        except Exception as e:
            print(f"\nError processing {filename}: {e}")
            
            print("Detailed Traceback:")
            traceback.print_exc()



print(f"Successfull count: {successfull_count}")
print(f"Failed count: {failed_count}")
exit("terminated successfully")
# Write the extracted resume data to the JSON file
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(resume_text_array, file, ensure_ascii=False, indent=4)

print(f"\nTotal records processed: {processed_count}")
print("-" * 150)
print(f"Extraction complete. Results saved in {output_file}")
