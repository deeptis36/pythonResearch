import spacy

# Load the trained model
nlp = spacy.load("ner_model")

# Example text for prediction
text = "John Doe is a software engineer at XYZ Corp."

# Process the text using the model
doc = nlp(text)

print(doc.ents)
# Extract and print entities
for ent in doc.ents:
    print(f"{ent.text} ({ent.label_})")
