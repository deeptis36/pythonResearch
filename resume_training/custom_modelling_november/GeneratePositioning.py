import spacy
import re
from fuzzywuzzy import fuzz
from data import skill_array, roles_array,resume_classification,work_keywords
from getName import get_name
from rapidfuzz import process, fuzz
from getWorkExperience import get_professional_summary

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




def get_position(key, text):
    """
    Finds the position of the key in the text.

    Parameters:
        key (str): The key to search for in the text.
        text (str): The text to search within.

    Returns:
        tuple: A tuple containing the start and end index of the key if found, otherwise None.
    """
    if not key or not text:
       
        return None

    # Use regex to find the key in the text
    pattern = re.escape(key)  # Escape any special characters in the role
    pattern = r'\b' + re.escape(key) + r'\b' 
    match = re.search(pattern, text, re.IGNORECASE)
   
    if match:
        return [match.start(), match.end()]
   
    return None
def get_employer_position_from_text(key, text):
    """
    Finds the position of the key in the text.

    Parameters:
        key (str): The key to search for in the text.
        text (str): The text to search within.

    Returns:
        tuple: A tuple containing the start and end index of the key if found, otherwise None.
    """
    if not key or not text:
       
        return None

    # Use regex to find the key in the text
    pattern = re.escape(key)  # Escape any special characters in the role
    pattern = re.escape(key)
    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return [match.start(), match.end()]
   
     
    return None


def remove_date_section(match_str):
    """
    Removes date-like sections (e.g., "Feb 2024 – Till Date") from the string.

    Parameters:
        match_str (str): The input string containing a potential date section.

    Returns:
        str: The string without the date section.
    """
    # Regex pattern to match date formats
    date_pattern = r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{4}\s*(–|to)?\s*(Till Date|\d{4})?\b"
    
    # Remove the date section
    cleaned_str = re.sub(date_pattern, '', match_str).strip()
    
    # Remove extra spaces if the date was at the end
    cleaned_str = re.sub(r'\s+', ' ', cleaned_str)
    
    return cleaned_str


def get_employer_position(key, text):

    
    text_lower = text.lower()
    key_lower = key.lower()
    
    employer_position = get_employer_position_from_text(key, text)

    if employer_position is not None:
        return employer_position 
    
    for line in text.split("\n"):        
        best_match = process.extractOne(key_lower, [line], scorer=fuzz.partial_ratio)
        if best_match and best_match[1] > 75:           
            match_str = remove_date_section( best_match[0])
            match_str1 = best_match[1] 
                    
            match_split = match_str.split(":")
            if len(match_split) > 1:
                key = match_split[1].strip()
            else:
                key = match_split[0].strip()           
            break
    
    employer_position = get_employer_position_from_text(key, text)
   
    return employer_position

def get_date_position(date, text):
    data_split = date.split("-")
    
    start_date = data_split[0]
    end_date = data_split[1]
    
    pattern_start = re.escape(start_date).replace(r"\s", r"\s*")  # Replace \s to \s* for flexible spaces
    pattern_end = re.escape(end_date).replace(r"\s", r"\s*")

    match_start = re.search(pattern_start, text, re.IGNORECASE)
    match_end = re.search(pattern_end, text, re.IGNORECASE)
    
    if match_start and match_end:
        return [match_start.start(), match_end.end()]
    
    return None


def get_position_entity(entities,text):
    
    main_entities = []
    for entity in entities:
        temp_entity = []
        for key in entity:
            role = key.get('role')
            date = key.get('date')
            employer = key.get('employer')

            location_role = get_employer_position(role,text)
           
            location_employer = get_employer_position(employer,text)
          
            location_date = get_date_position(date,text)
            
            
            role_enitity = {
                "label": "ROLE",
                "start": location_role[0],
                "end": location_role[1],
                "word": role,
                "entity": "ROLE"
            }
            if len(location_employer) > 0:
                employer_entity = {
                    "label": "EMPLOYER",
                    "start": location_employer[0],
                    "end": location_employer[1],
                    "word": employer,
                    "entity": "EMPLOYER"
                }
                main_entities.append(employer_entity)
            date_entity = {
                "label": "DATE",
                "start": location_date[0],
                "end": location_date[1],
                "word": date,
                "entity": "DATE"
            }

            main_entities.append(role_enitity)
            
            main_entities.append(date_entity)
 
    return main_entities
            
  


def get_professional(text):
    data = get_professional_summary(text)
   
    if len(data) > 0:       
        position_data = get_position_entity(data,text)
        
        return position_data
    return []


  








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







