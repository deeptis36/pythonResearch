import re
from data import roles_array,software_tools,skill_array
import spacy

# Load the spaCy model
nlp = spacy.load('en_core_web_md')




def extract_employers_only(text):

    
    # Preprocess text: Remove special characters and normalize spaces
    clean_text = re.sub(r'[^\w\s,.]', ' ', text)  # Remove special chars except commas and spaces
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()  # Normalize spaces
    
    # Apply NER model
    doc = nlp(clean_text)
    employers = []


    pattern = r'client:\s*([^,]+)'
    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        client_name = match.group(1)  # Ex        
        add_if_unique(employers, client_name)

    employer_keywords = [
        "Ltd", "Pvt Ltd", "Pvt Ltd.", "Private Limited", "Solutions", "Solution",
        "Inc", "Corp", "Corporation", "LLC", "Technologies", "Consultants",
        "Research and Services", "Group", "Groups", "Industries", "Company","technology"
    ]
    # Define an extended regex pattern for employer-related keywords and phrases
    pattern_str = r'\b(?:' + '|'.join(re.escape(keyword) for keyword in employer_keywords) + r')\b'
    patterns = re.compile(pattern_str, re.IGNORECASE)

    # Check for NER-identified entities
    for ent in doc.ents:
        if ent.label_ in {"ORG", "PERSON"} or patterns.search(ent.text):
            add_if_unique(employers, ent.text)

    # Apply regex to raw text for additional matches (no need for second re.findall)
    matches = re.findall(pattern_str, clean_text, re.IGNORECASE)
    
    for match in matches:
        add_if_unique(employers, match.strip())

    return employers


def add_if_unique(employers, candidate):
    """
    Add a candidate string to the employers list if it is not a substring
    of any existing string, and no existing string is a substring of it.
    """
    candidate = candidate.lower().strip()  # Normalize case and strip spaces

    # for existing in employers:
    #     if candidate in existing.lower() or existing.lower() in candidate:
    #         return  # Skip adding if partial match found

    employers.append(candidate)
def get_employer(text):

    words = text.split()

    if(text == "" or len(words) >= 25):
        return []
    employers = [] 
    entry = text.strip()  # Remove leading/trailing whitespace
    if entry and not any(role.lower() in entry.lower() for role in roles_array):
        employers = extract_employers_only(entry)
    return " ".join(employers)


def is_skill(candidate, skill_array):
    """
    Check if a candidate string matches any skill in the skill_array.
    """
    candidate_lower = candidate.lower()
    for skill in skill_array:
        if skill.lower() in candidate_lower or candidate_lower in skill.lower():
            return True
    return False

# Test the function
# if __name__ == "__main__":
#     input_text = "I am a carpenter with experience ."
#     role = get_employer(input_text)
#     if role:
#         print(f"Matched Role: {role}")
#     else:
#         print("No role matched.")
