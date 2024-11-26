import spacy

# Load the trained model
nlp = spacy.load("./output/model-last")

# Parse a sample resume
resume_text = """
John Doe
Python Developer
Skills: Python, Machine Learning, Data Science, REST APIs
Experience: 5 years
Education: Bachelor of Computer Science
"""
doc = nlp(resume_text)

# Display extracted entities
print("Entities detected:")
for ent in doc.ents:
    print(f"{ent.label_}: {ent.text}")
