import spacy
from spacy.training.example import Example
from spacy.training import offsets_to_biluo_tags

# Load a blank English model
nlp = spacy.blank("en")

# Example training data with improved offsets
train_data = [
    ("Jane Doe Email: jane.doe@example.com Phone: +9876543210", {'entities': [(0, 8, 'NAME'), (14, 34, 'EMAIL'), (41, 55, 'PHONE')]}),
    ("John Smith john.smith@domain.com Contact: 124567890 Skills: Python, Java, Machine Learning", {'entities': [(0, 10, 'NAME'), (11, 33, 'EMAIL'), (43, 54, 'PHONE'), (63, 85, 'SKILLS')]}),
]

# Add the NER pipeline if not present
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner", last=True)

# Add new labels to the NER model
for _, annotations in train_data:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

# Initialize the model
nlp.initialize()

# Check each example for alignment
for text, annotations in train_data:
    doc = nlp.make_doc(text)
    entities = annotations["entities"]
    tags = offsets_to_biluo_tags(doc, entities)
    print(f"Text: {text}")
    print(f"Entities: {entities}")
    print(f"BILUO tags: {tags}")
    print("-" * 30)

# Continue with training if alignment is correct
optimizer = nlp.initialize()

# # Training loop
# for itn in range(10):
#     losses = {}
#     for text, annotations in train_data:
#         example = Example.from_dict(nlp.make_doc(text), annotations)
#         nlp.update([example], sgd=optimizer, drop=0.35, losses=losses)
#     print(f"Iteration {itn} Losses: {losses}")




from spacy import displacy

# Load pre-trained model or fine-tune your own
nlp = spacy.load("en_core_web_sm")

# Parse a sample resume text
resume_text = """John Doe
Phone: 123-456-7890
Email: john.doe@example.com
Experience: Software Developer at ABC Corp from 2018-2023
Skills: Python, Machine Learning, Data Science
Education: B.Tech in Computer Science, XYZ University"""

# Process the text
doc = nlp(resume_text)

# Extract entities (e.g., Name, Email, Phone)
for ent in doc.ents:
    print(ent.text, ent.label_)

# Example Output:
# John Doe PERSON
# 123-456-7890 PHONE
# john.doe@example.com EMAIL
# Software Developer JOB
# ABC Corp ORG
