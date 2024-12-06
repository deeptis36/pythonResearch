import re
from data import roles_array,resume_classification
import spacy
from fuzzywuzzy import fuzz

# Load the SpaCy model
try:
    nlp = spacy.load('en_core_web_md')
except OSError:
    raise ImportError("SpaCy model 'en_core_web_md' not found. Run `python -m spacy download en_core_web_md` to install it.")


def extract_role_from_pattern(line):
    """
    Extract roles from predefined patterns in a line.
    Args:
        line (str): The input line to search for patterns.
    Returns:
        str or bool: Extracted role or False if no match found.
    """
    patterns = ["worked as", "role:", "designation:"]  # Patterns to match
    for pattern in patterns:
        regex = r"{}\s*(.*)".format(re.escape(pattern))
        match = re.search(regex, line, re.IGNORECASE)
        if match:
            return match.group(1).strip()  # Return the role after the matched pattern
    return False


def retrieve_roles_from_text(text):
    """
    Extract roles using NLP entities and patterns from text.
    Args:
        text (str): Input text to analyze.
    Returns:
        list: List of extracted roles.
    """
    roles = []  # To store identified roles
    lines = text.split("\n")
    for line in lines:
        doc = nlp(line)
        for ent in doc.ents:
            if ent.label_ in ["JOB_TITLE", "ROLE", "PERSON"]:  # Adjust labels as needed
                roles.append(ent.text)
    return roles



def retrieve_role(text, roles_array):
    text_lower = text.lower()  # Convert text to lowercase for case-insensitive matching
   
    for tmprole in roles_array:
            if(text.replace(" ", "").lower() == tmprole.replace(" ", "").lower()):
                return tmprole

    # Check for an exact match in roles_array
    if text_lower in roles_array:
        return text  # Return exact match

    # Check for partial matches using regex for whole word matching
    for role in roles_array:
        if re.search(r'\b' + re.escape(role.lower()) + r'\b', text_lower):
           
            return role  # Return the matched role

  
    return False 



def get_role(resume_text):

    text_array = resume_text.split("|")
    
    for text in text_array:
        if any(keyword.lower() in text.lower() for keyword in resume_classification):
            return False
       
        role = retrieve_role(text, roles_array)
        if role:
            return role
      
        role_from_pattern = extract_role_from_pattern(text)
        
        if role_from_pattern:
            return role_from_pattern

        # Step 2: Extract roles using NLP entity recognition
        roles_from_nlp = retrieve_roles_from_text(text)

        text_lower = text.lower()

        max_similarity_threshold = 80  # Set threshold for fuzzy matching

        # Step 3: Exact match using regex

       
        for tmprole in roles_array:
            if(text.replace(" ", "").lower() == tmprole.replace(" ", "").lower()):
                return tmprole
            
        
        for drole in roles_array:
            if re.search(r'\b' + re.escape(drole.lower()) + r'\b', text_lower):           
                return drole  # Exact match found

        # Step 4: Fuzzy matching for approximate matches
        best_match = None
        highest_similarity = 0
        for role in roles_array:
            similarity = fuzz.ratio(role.lower(), text_lower)
            if similarity > highest_similarity and similarity >= max_similarity_threshold:
                best_match = role
                highest_similarity = similarity

    
        if best_match:
            return best_match

    return False  # No match found


# Test the function
if __name__ == "__main__":
    input_text = "I worked as a software engineer with 5 years of experience."
    matched_role = get_role(input_text)
    if matched_role:
        print(f"Matched Role: {matched_role}")
    else:
        print("No role matched.")
