import os
import re
import json
from resumeText import get_resume_text

# Define the folder path where the resumes are stored
folder_path = "files/"

# Array to store resume data (both text and extracted entities)
resume_data_array = []

# Iterate through each file in the specified folder
for filename in os.listdir(folder_path):
    # Construct full file path
    file_path = os.path.join(folder_path, filename)
    
    # Check if the file is a resume (optional filter by file extension)
    if filename.endswith(".pdf"):  # Adjust if other formats are needed
        print(f"Processing File: {filename}")
        
        # Extract text from the resume file
        resume_text = get_resume_text(file_path)
        
        # Extract entities using regular expressions
        entities_array = re.findall(r'\w+', resume_text)  # Modify regex as needed
        
        # Append structured data (text and entities) to the main array
        resume_data_array.append({
            "resume_text": resume_text,  # Full resume text
            "entities": [entities_array]  # Entities array and an additional empty array
        })

# Define the JSON output file path
output_file = "resume_data.json"

# Save resume data to a JSON file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(resume_data_array, f, ensure_ascii=False, indent=4)

print(f"Resume data successfully saved to {output_file}")
