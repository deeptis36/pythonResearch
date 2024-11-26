import spacy
import re
from fuzzywuzzy import fuzz
from data import skill_array, roles_array
from getName import get_name

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Regular expressions for email and phone
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
# phone_pattern = r'(\+?\d{1,4}[ -]?)?(\(?\d{1,4}\)?[ -]?)?\d{1,4}[ -]?\d{1,4}[ -]?\d{1,4}'
phone_pattern = r'(\+?\d{1,4}[ .-]?)?(\(?\d{1,4}\)?[ .-]?)?\d{1,4}[ .-]?\d{1,4}[ .-]?\d{1,4}'

entity_labels = [
    "PERSON", "ORG", "GPE", "LOC", "FAC", "DATE", "TIME",
    "PERCENT", "MONEY", "QUANTITY", "ORDINAL", "CARDINAL",
    "PRODUCT", "EVENT", "WORK_OF_ART", "LAW", "LANGUAGE",
    "NORP", "EMAIL", "PHONE"
]

def get_word_positions(resumetextInput):
    resumetext = resumetextInput.strip(":")
    # Split resume text into lines
    resumetext = resumetext.split("\n")
  
    # Initialize an empty dictionary to store all entities
    entity_dict = {}
    # Iterate through each line in the resume text
    for text in resumetext:
        doc = nlp(text)  # Process each line with spaCy's NLP
      
        # Extract named entities (e.g., name, email, phone) using spaCy
        for ent in doc.ents:
            entity = ent.label_
            if ent.label_ in entity_labels:
                # Check if the entity text matches any skill from the skill_array (case insensitive)
                if ent.text.lower() in [skill.lower() for skill in skill_array]:
                    entity = "SKILLS"
                    ent.label_ = "SKILLS"
                else:
                    # Fuzzy matching block (only executed when no exact match is found)
                    threshold = 80
                    for skill in skill_array:
                        similarity = fuzz.ratio(ent.text.lower(), skill.lower())
                        if similarity >= threshold:
                            entity = "SKILLS"
                            ent.label_ = "SKILLS"
                            break

                # Check if the entity text matches any role from the roles_array (case insensitive)
                if ent.text.lower() in [role.lower() for role in roles_array]:
                    entity = "ROLE"
                    ent.label_ = "ROLE"

                # Initialize the list if the entity is not yet in the dictionary
                if entity not in entity_dict:
                    entity_dict[entity] = []
                matches = re.finditer(re.escape(ent.text), resumetextInput)
                for match in matches:
                    entity_dict[entity].append({
                        "label": ent.label_,
                        "start": match.start(),
                        "end": match.end(),
                        "word": match.group(),
                        "entity": entity
                    })
               
        # Custom handling for emails and phone numbers using regex

        # Find all emails using regex
        emails = re.finditer(email_pattern, text)
        for email in emails:
            if "EMAIL" not in entity_dict:
                entity_dict["EMAIL"] = []
            entity_dict["EMAIL"].append({
                "label": "EMAIL",
                "start": email.start(),
                "end": email.end(),
                "word": email.group(),
                "entity": "EMAIL"
            })

  

    return entity_dict
# Function to extract skills from the entity dictionary
def get_skills(entity_dict):
    # Check if "SKILLS" is present in the entity_dict and return the skills
    skills = []
    if "SKILLS" in entity_dict:
        for skill in entity_dict["SKILLS"]:
            skills.append(skill)  # Append the skill word (entity text)
    return skills


def replace_colon_with_space(text):
    # List of items to replace with an equal length of spaces
    replacable_to_null = ["E-mail ID", "Name", "email id", "E-mail", ":"]
    
    for item in replacable_to_null:
        # Replace each unwanted string with spaces of the same length
        text = text.replace(item, " " * len(item))
    
    # Return the cleaned-up text
    return text




def get_phone_entity(resumetext):
    phone_objects = []  # Collect all matches in a list

    phone_numbers = re.finditer(phone_pattern, resumetext)

    for phone in phone_numbers:
        if len(phone.group()) > 9:  # Optional: Enforce minimum length
            phone_objects.append({
                "label": "PHONE",
                "start": phone.start(),
                "end": phone.end(),
                "word": phone.group(),
                "entity": "PHONE"
            }) 
            return phone_objects
    return phone_objects
     # Return all matches



def clean_text(text):
    # Remove everything after the first comma or newline
    split_text = re.split(r'[,\n]', text)
    # If there's no comma or newline, the split will result in a single part, so no need for further handling
    cleaned_text = split_text[0].strip()
    
    return text








def get_name_entity(text):
    text = text.lower()
    name = get_name(text)
    

    if name == "Name not found":
        return {"message": "Name not found"}
    
    matches = re.finditer(name, text)
   
    for match in matches:
       
        name_object = {
                "label": "NAME",
                "start": match.start(),
                "end": match.end(),
                "word": name,
                "entity": "NAME"
            }
       
        return name_object







