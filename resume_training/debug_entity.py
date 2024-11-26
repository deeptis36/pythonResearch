import spacy
from spacy.training import offsets_to_biluo_tags

# Load pre-trained model
nlp = spacy.load("en_core_web_sm")

# Define your text and corrected entity annotations
text = "John-Doe\nEmail: john.doe@example.com\nPhone: +1234567890"

# Create the document object from the text
doc = nlp.make_doc(text)

# Tokenize the text and print tokens with their span positions
for token in doc:
    print(f"Token: {token.text} | Start: {token.idx} | End: {token.idx + len(token.text)}")

# Corrected entity spans (based on tokens observed)
entities = [(0, 8, "NAME"), (9, 34, "EMAIL"), (35, 55, "PHONE")]

# Convert the entity annotations to BILUO tags
biluo_tags = offsets_to_biluo_tags(doc, entities)

# Print the resulting BILUO tags
print(biluo_tags)
