import spacy
from spacy.training.example import Example
import random
import json

# Load the blank English model
nlp = spacy.blank("en")
def evaluate_model(model, dev_data):
    correct = 0
    total = 0
# Load your training and development data
with open("train_data_split.json", "r", encoding="utf-8") as f:
    train_data = json.load(f)

with open("dev_data.json", "r", encoding="utf-8") as f:
    dev_data = json.load(f)

# Add NER pipeline if not already present
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner", last=True)  # This is the correct way to add NER

# Add labels to the NER model
for _, annotations in train_data:
    for ent in annotations["entities"]:
        ner.add_label(ent[2])  # Add each label to the NER model

# Set up the training loop
optimizer = nlp.begin_training()

# Training for a set number of iterations
for iteration in range(10):
    random.shuffle(train_data)  # Shuffle the training data for better generalization
    losses = {}
    
    # Loop through training data
    for text, annotations in train_data:
        doc = nlp.make_doc(text)
        
        try:
            example = Example.from_dict(doc, annotations)  # Create an example from the text and annotations
            print(example)
            nlp.update([example], losses=losses)  # Update the model with the new example
        except ValueError as e:
            print()
            print(f"Skipping example due to error: {e}")
            # continue  # Skip this example if an error occurs
    
    print(f"Iteration {iteration + 1}, Losses: {losses}")
    
    # Optionally evaluate after each iteration (if needed)
    evaluate_model(nlp, dev_data)

# Final model evaluation after training
evaluate_model(nlp, dev_data)

# Save the trained model
nlp.to_disk("ner_model")

print("Training complete and model saved.")

# Evaluate the model on the dev set
def evaluate_model(model, dev_data):
    correct = 0
    total = 0
    
    for text, annotations in dev_data:
        doc = model.make_doc(text)
        for ent in annotations["entities"]:
            total += 1
            span = doc.char_span(ent[0], ent[1], label=ent[2])
            if span is not None and span.label_ == ent[2]:
                correct += 1
    
    accuracy = correct / total
    print(f"Evaluation accuracy: {accuracy * 100:.2f}%")
