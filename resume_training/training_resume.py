import spacy
from spacy.training import offsets_to_biluo_tags

# Load pre-trained model
nlp = spacy.load("en_core_web_sm")

# Define your text and entity annotations
text = "John-Doe\nEmail: john.doe@example.com\nPhone: +1234567890"
entities = [(0, 8, "NAME"), (16, 36, "EMAIL"), (44, 55, "PHONE")]

# Create a doc object from the text
doc = nlp.make_doc(text)

# Convert the entity annotations to BILUO tags
biluo_tags = offsets_to_biluo_tags(doc, entities)

# Print BILUO tags
print(biluo_tags)
