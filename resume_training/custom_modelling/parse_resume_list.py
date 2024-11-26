import spacy
import os
import re
import json
from datetime import datetime
from resumeText import get_resume_text

# Load the trained model
nlp = spacy.load("./output/model-last")
folder_path = "files/" 

# Generate a timestamped output file name
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"results/output_{current_datetime}.txt"

# Ensure the 'results' directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Initialize a counter for processed records
processed_count = 0

# Open the output file in write mode
with open(output_file, "w", encoding="utf-8") as file:
    for filename in os.listdir(folder_path):
        # Construct full file path
        file_path = os.path.join(folder_path, filename)
        
        # Check if the file is a resume (optional filter by file extension)
        if filename.endswith(".pdf") or filename.endswith(".doc") or filename.endswith(".docx"):  # Adjust as needed
            file.write(f"\nProcessing File: {filename}\n")
            file.write("-" * 150 + "\n")
            
            print(f"\nProcessing File: {filename}")
            
            # Extract text from the resume file
            resume_text = get_resume_text(file_path)
            
            if resume_text is None:
                # Skip the file if text extraction failed
                file.write(f"Error: Could not extract text from {filename}\n")
                print(f"Error: Could not extract text from {filename}")
                continue  # Skip this file and move to the next one
            
            try:
                doc = nlp(resume_text)
            except Exception as e:
                # Catch any exception raised by spaCy
                file.write(f"Error processing text with spaCy: {str(e)}\n")
                print(f"Error processing text with spaCy: {str(e)}")
                file.write(f"Error processing text with spaCy: {str(e)}")
                  # Skip this file and move to the next one

            # Display extracted entities
            file.write("Entities detected:\n")
            for ent in doc.ents:
                file.write(f"{ent.label_}: {ent.text}\n")
                print(f"{ent.label_}: {ent.text}")
            
            file.write("\n" + "-" * 150 + "\n")
            print("\n" + "-" * 150 + "\n")
            
            # Increment processed count
            processed_count += 1

    # Write the total number of records processed at the end of the file
    file.write(f"\nTotal records processed: {processed_count}\n")

print(f"Extraction complete. Results saved in {output_file}")
