import spacy
from spacy.tokenizer import Tokenizer
from spacy.tokens import Token
from spacy.attrs import ORTH, NORM
from resume_parser import resumeparse


# Load the English model
nlp = spacy.load("en_core_web_sm")

# Example: Tokenizer with custom exceptions
def add_custom_token_exceptions(nlp):
    # Add custom exceptions: these are only modifying ORTH and NORM
    nlp.tokenizer.add_special_case("custom_word", [{ORTH: "custom_word"}])
    nlp.tokenizer.add_special_case("example", [{ORTH: "example"}])

# Add custom exceptions (tokenization logic)
add_custom_token_exceptions(nlp)

# Load custom model (ensure this model is compatible with spaCy)
custom_model_path = "/var/www/html/ml/app/scripts/resume_parser_effort/degree/model"

def set_custom_attributes(doc):
    # Set custom attributes on tokens after tokenization
    for token in doc:
        # Ensure the custom POS attribute is only set once
        if not token.has_extension('custom_pos'):
            token.set_extension('custom_pos', default=None)
        
        # Apply a custom POS tag after tokenization
        if token.text == "custom_word":
            token._.custom_pos = 'noun'  # Custom POS for 'custom_word'
        elif token.text == "example":
            token._.custom_pos = 'noun'  # Custom POS for 'example'
        else:
            token._.custom_pos = 'other'  # Default POS tag for other tokens
    return doc

# Load the custom model
try:
    # custom_nlp2 = spacy.load(custom_model_path)
    print("Custom model loaded successfully!")
except Exception as e:
    print("Failed to load custom model:", e)

# Process a sample text (using the default 'nlp' model for tokenization)
doc = nlp("This is an example sentence with custom_word.")

# Apply custom attributes after tokenization
doc = set_custom_attributes(doc)

# Print out tokens and their custom attributes
for token in doc:
    print(f"Token: {token.text}, Custom POS: {token._.custom_pos}")
