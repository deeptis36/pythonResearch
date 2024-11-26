import spacy
from spacy.training import Example
import csv
import random  # <-- Add this import for random module
from tqdm import tqdm
nlp = spacy.load("en_core_web_sm")
print(nlp.pipe_names)
print(nlp)
# Function to load the data from CSV
def load_data(file_path):
    texts = []
    annotations = []

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            text = row['Text']
            entities = eval(row['Entities'])  # Convert the string representation of the list to an actual list of tuples
            texts.append(text)
            annotations.append(entities)
    
    return texts, annotations

# Function to convert data into Example format for SpaCy training
def convert_to_examples(texts, annotations, nlp):
    examples = []
    for text, entities in zip(texts, annotations):
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, {"entities": entities})
        examples.append(example)
    return examples

# Train function
def train_ner_model(train_data, n_iter=10, output_dir="output_model"):
    # Load pre-trained SpaCy model
   
    
    # Create a new NER component if it doesn't exist
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe("ner")
        nlp.add_pipe(ner, last=True)
    else:
        ner = nlp.get_pipe("ner")

    # Add labels to the NER component
    for _, annotations in train_data:
        for ent in annotations:
            ner.add_label(ent[2])  # Add entity label like "NAME", "EMAIL", "PHONE"
    
    # Start training
    optimizer = nlp.begin_training()
    
    for itn in range(n_iter):
        print(f"Training iteration {itn + 1}")
        losses = {}
        # Shuffle and create minibatches
        random.shuffle(train_data)  # Shuffle the data using random.shuffle()
        for text, annotations in tqdm(train_data, desc="Training", unit="batch"):
            example = Example.from_dict(nlp.make_doc(text), {"entities": annotations})
            # Update the model with the example
            nlp.update([example], losses=losses)
        print(f"Losses at iteration {itn + 1}: {losses}")

    # Save the model to disk
    nlp.to_disk(output_dir)
    print(f"Model saved to {output_dir}")

# Main function
if __name__ == "__main__":
    # Load training data from CSV file
    train_data_file = "training_data.csv"
    texts, annotations = load_data(train_data_file)

    # Convert data to SpaCy Example format
    train_data = list(zip(texts, annotations))
    
    # Train the model
    train_ner_model(train_data, n_iter=10, output_dir="trained_model")
