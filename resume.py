import spacy

# Load the model using its full name
nlp = spacy.load("en_core_web_sm")

# Test the model with some text
doc = nlp("This is a sample text.")
for token in doc:
    print(token.text, token.pos_, token.dep_)