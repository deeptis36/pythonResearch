import spacy
import os
import json
from datetime import datetime
from resumeText import get_resume_text
from sklearn.model_selection import train_test_split

# Load the trained model
nlp = spacy.load("./output/model-best")
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
            
            # Initialize empty lists for texts and labels
            texts = []
            labels = []
            
            for item in resume_text:
                text = item[0]  # Extract the text
                
                # Check if 'entities' exist and is not empty
                if len(item) > 1 and 'entities' in item[1] and item[1]['entities']:
                    entity_labels = item[1]['entities']
                else:
                    entity_labels = []  # Set empty list if no entities are found
                
                texts.append(text)
                labels.append(entity_labels)

            # Split the data into training and test sets
            X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

            # Print results for checking (console output)
            print("Training set:")
            print(X_train[:3])  # Displaying first 3 training samples for verification
            print(y_train[:3])

            print("\nTest set:")
            print(X_test[:3])  # Displaying first 3 test samples for verification
            print(y_test[:3])

            # Write results to the file
            file.write("Training set:\n")
            file.write(json.dumps(X_train[:3], indent=2))  # Write first 3 training samples
            file.write("\nEntities:\n")
            file.write(json.dumps(y_train[:3], indent=2))  # Write corresponding entity labels

            file.write("\nTest set:\n")
            file.write(json.dumps(X_test[:3], indent=2))  # Write first 3 test samples
            file.write("\nEntities:\n")
            file.write(json.dumps(y_test[:3], indent=2))  # Write corresponding entity labels

            file.write("\n" + "-" * 150 + "\n")
        
            # Increment processed count
            processed_count += 1

    # Write the total number of records processed at the end of the file
    file.write(f"\nTotal records processed: {processed_count}\n")

print(f"Extraction complete. Results saved in {output_file}")
