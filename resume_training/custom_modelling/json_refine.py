import random
from venv import logger
import spacy
from spacy.training import Example
from spacy.tokens import DocBin
import json
import logging
# Load the JSON file
with open('train_data.json', 'r') as f:
    train_data_set = json.load(f)


def check_resume_data_with_entities(resume_text, entities):
    # Check if the resume text and entities match
    print(resume_text)
    print("===============================================================================================================")
    for entity in entities:
        start, end, label = entity
     
        substring = resume_text[start:end]
        print(start , '|',end,'|', label, '|', substring)
        print()

train_data = train_data_set[0]
resume_text = train_data[0]  # First element is the resume text

    # Extract entities from the second part (the dictionary)
entities = train_data[1].get("entities", [])
check_resume_data_with_entities(resume_text, entities)


