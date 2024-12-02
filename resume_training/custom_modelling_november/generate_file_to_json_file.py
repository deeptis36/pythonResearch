import spacy
import os
import json
from datetime import datetime
from resumeText import get_resume_text
from GeneratePositioning import get_word_positions,get_skills,get_name_entity,get_phone_entity,get_professional
from employer import get_employer
# Generate a timestamped output file name
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"json/output_{current_datetime}.json"

# Ensure the 'json' directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Initialize a counter for processed records
processed_count = 0
folder_path = "files"

# Array to hold extracted resume data
resume_text_array = []

# Process each file in the folder
for filename in os.listdir(folder_path):
    # Construct full file path
    file_path = os.path.join(folder_path, filename)
    
    # Check if the file is a resume (optional filter by file extension)
    if filename.endswith((".pdf", ".doc", ".docx")):  # Adjust as needed
      
        
        # Extract text from the resume file
        try:
          
            entities = []

            entities.append({"resume": filename})
            #name
            
            terminating_file_name = "Gokul_CV_1124_1.docx"
            terminating_file_name = "Resume_201124135354_Resuem-Savitha_Gadam.docx"
            terminating_file_name = "Resume_201124140014_.docx"
           
            if True and  filename == terminating_file_name:
               
                print(f"\n***************************Processing File: {filename} *************************************")
        
                resume_text = get_resume_text(file_path)
              
                entity_dict = get_word_positions(resume_text)
               
                entity_skill = get_skills(entity_dict)
               
                enitity_name = get_name_entity(resume_text)
                entities.append(enitity_name)
               
                entity_phone = get_phone_entity(resume_text)
                for phone in entity_phone:
                    entities.append(phone)

                email = entity_dict.get("EMAIL")[0]
                entities.append(email)

                #append skill
                for skill in entity_skill:
                    entities.append(skill)
                
          
               
                professional_entity = get_professional(resume_text)

                # print(entities)


                print("="*150)
                print(professional_entity)
                resume_data = {
                    "resume_text": resume_text,
                    "entities": entities,  # Adjust this to store parsed entities if needed
                }
                resume_text_array.append(resume_data)
                # exit(0)
           
                      
            processed_count += 1
        except Exception as e:
            print(f"Error processing {filename}: {e}")

exit("terminated successfully")
# Write the extracted resume data to the JSON file
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(resume_text_array, file, ensure_ascii=False, indent=4)

print(f"\nTotal records processed: {processed_count}")
print("-" * 150)
print(f"Extraction complete. Results saved in {output_file}")
