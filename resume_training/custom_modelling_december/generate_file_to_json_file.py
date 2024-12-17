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
output_file = f"json/set2_{current_datetime}.json"
output_file_name_list = f"json/file_removal_list.json"

# Ensure the 'json' directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Initialize a counter for processed records
processed_count = 0
folder_path = "resumesets"
folder_path = "files"

# Array to hold extracted resume data
resume_text_array = []
file_removal_array = []
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
            
            terminating_file_name = "Resume_091224140106_.pdf"
            terminating_file_name ="Resume_201124140703_.docx"
          
            if True or  filename == terminating_file_name:
               
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
               
                # print(f"Name: {enitity_name}")
                # print(f"Phone: {entity_phone}")
                # print(f"Email: {email_entity}")
                # print(f"Skills: {entity_skill}")
                # print(f"Professional Summary: {professional_entity}")
                if len(professional_entity) > 0 and   email_entity and len(entity_skill) > 0:
                    successfull_count += 1
                    file_name_array.append(file_path)
                    
                    entities.append(enitity_name)

                    if len(entity_phone) > 0 :
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
                    file_removal_array.append(file_path)
                    

                else:
                    failed_count += 1
                
                
                print("="*150)
                # exit(0)
           
                      
            processed_count += 1
        except Exception as e:
            print("\n","_"*150)
            print(f"\nError processing {filename}: {e}")
            
            print("Detailed Traceback:")
            traceback.print_exc()
            print("\n","_"*150)


print(resume_text_array)
print(f"\n\nSuccessfull count: {successfull_count}")
print(f"Failed count: {failed_count}")
# exit("\n\nTerminated")
# Write the extracted resume data to the JSON file
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(resume_text_array, file, ensure_ascii=False, indent=4)

with open(output_file_name_list, "w", encoding="utf-8") as file:
    json.dump(file_removal_array, file, ensure_ascii=False, indent=4)
print(f"\nTotal records processed: {processed_count}")
print("-" * 150)
print(f"Extraction complete. Results saved in {output_file}")
