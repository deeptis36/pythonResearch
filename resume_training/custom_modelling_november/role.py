import re
from data import roles_array
import spacy
from fuzzywuzzy import fuzz
# Load the spaCy model
nlp = spacy.load('en_core_web_md')


def extract_role_from_pattern(line):
    # List of patterns to check for
    patterns = ["worked as", "role:", "designation:"]
    
    # Regular expression to match each pattern followed by the role
    for pattern in patterns:
        regex = r"{}\s*(.*)".format(re.escape(pattern))  # Escape special characters in the pattern
        
        # Search for the pattern
        match = re.search(regex, line, re.IGNORECASE)

        if match:
            return match.group(1).strip()  # Return the role (everything after the pattern)

    return False  # If no match found, return this    
def get_role(text):
    """
    Matches roles based on predefined role list using exact match and spaCy similarity.
    Args:
        text (str): Input string.
    Returns:
        str: Matched role, or None if no match is found.
    """



    role = extract_role_from_pattern(text)
    if role:
        return role



    text_lower = text.lower()
    max_similarity_threshold = 80 
    # Step 1: Check for exact matches using regex
    for role in roles_array:

        if re.search(r'\b' + re.escape(role.lower()) + r'\b', text_lower):
            # print("Exact Match:", role)
            return role  # Exact match found

    # Step 2: Apply fuzzy logic for approximate matches
    best_match = None
    highest_similarity = 0

    for role in roles_array:
        similarity = fuzz.ratio(role.lower(), text_lower)
        if similarity > highest_similarity and similarity >= max_similarity_threshold:
            best_match = role
            highest_similarity = similarity

    # If a match is found with fuzzy logic
    if best_match:
        # print("Fuzzy Match:", best_match)
        return best_match
    
    return False

# Test the function
if __name__ == "__main__":
    input_text = "I am a carpenter with experience ."
    role = get_role(input_text)
    if role:
        print(f"Matched Role: {role}")
    else:
        print("No role matched.")
