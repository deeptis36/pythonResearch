import random
from venv import logger
import spacy
from spacy.training import Example
from spacy.tokens import DocBin
import json
import logging
import sys
file = "json/sample.json"
# Load the JSON file
with open(file, 'r') as f:
    train_data = json.load(f)

# Load a blank model to convert the text to Doc objects
nlp = spacy.blank("en")

# Shuffle the data to avoid any bias
random.shuffle(train_data)

# Split into training and validation sets (80/20 split)
train_size = int(0.8 * len(train_data))
train_data_split = train_data[:train_size]
dev_data_split = train_data[train_size:]

# Convert to spaCy's Example format
train_examples = []
dev_examples = []

# Convert each item into the Example format for training data
for item in train_data_split:
    resume_text = item[0]  # First element is the resume text

    # Extract entities from the second part (the dictionary)
    entities = item[1].get("entities", [])
   

    annotations = {"entities": []}  # Initialize annotations as a dictionary

    # Extract entities and append them to annotations
    for entity in entities:
        start, end, label = entity
        annotations["entities"].append((start, end, label))


    # Create a Doc object using the resume text
    doc = nlp(resume_text)

    # Create an example from the doc and annotations
    try:
        example = Example.from_dict(doc, annotations)
        train_examples.append(example)

    except ValueError as e:
        logger.error(f"Skipping example due to error: {e}")
        # print(f"Skipping example due to error: {e}")
        
    # example = Example.from_dict(doc, annotations)
    
# Convert each item into the Example format for validation data
for item in dev_data_split:
    resume_text = item[0]  # First element is the resume text

    # Extract entities from the second part (the dictionary)
    entities = item[1].get("entities", [])

    annotations = {"entities": []}  # Initialize annotations as a dictionary

    # Extract entities and append them to annotations
    for entity in entities:
        start, end, label = entity
        annotations["entities"].append((start, end, label))

    # Create a Doc object using the resume text
    doc = nlp(resume_text)

    try:
        example = Example.from_dict(doc, annotations)
        dev_examples.append(example)
    except ValueError as e:        
        print(f"Skipping example due to error: {e}")
    # Create an example from the doc and annotations


# Save to .spacy format
train_spacy = "./train.spacy"
dev_spacy = "./dev_set.spacy"

print("\n"+"-"*150+"\n")

try:
    # Ensure train_examples and dev_examples are properly created
    if not train_examples or not dev_examples:
        raise ValueError("Training or validation examples are empty or not initialized.")

    # Extract Doc objects from Examples
    train_docs = [example.reference for example in train_examples]  # Extract Doc from Example
    dev_docs = [example.reference for example in dev_examples]  # Extract Doc from Example

    # Create DocBin for training and validation data
    train_db = DocBin(docs=train_docs)
    dev_db = DocBin(docs=dev_docs)
    print("DocBin objects created successfully.")

    # Save the data to disk
    train_db.to_disk(train_spacy)
    dev_db.to_disk(dev_spacy)

    print(f"Training data saved to {train_spacy}")
    print(f"Validation data saved to {dev_spacy}")

except ValueError as ve:
    print(f"ValueError: {ve}")
    sys.exit(1)
except FileNotFoundError as fnfe:
    print(f"FileNotFoundError: {fnfe}. Ensure the file path is correct.")
    sys.exit(1)
except PermissionError as pe:
    print(f"PermissionError: {pe}. Check file write permissions.")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)
else:
    print("Script executed successfully without errors.")
finally:
    print("Execution completed.")
print(f"Training data saved to {train_spacy}")
print(f"Validation data saved to {dev_spacy}")
