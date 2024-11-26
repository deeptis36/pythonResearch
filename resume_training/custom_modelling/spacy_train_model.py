import spacy
import json
from spacy.tokens import DocBin

nlp = spacy.blank("en")


def loadTrainData1():
    file = "json/sample.json"
    with open(file, "r", encoding="utf-8") as f:
        training_data = json.load(f)

    db = DocBin()
    i =0
    for text, annotations in training_data:
        doc = nlp.make_doc(text)
        ents = []
        spans = []  # Keep track of start-end positions to detect overlaps
        has_overlap = False  # Flag to check for overlaps
        if i ==1:
            continue
        for entity in annotations["entities"]:
            # Check for invalid spans
            # print(start, end, label)
            start = entity[0]
            end = entity[1] 
            label = entity[2]
        
            substring = text[start:end]
            print(start, end, label, substring)
        
            # continue
            # Check if the span is valid
            if start >= end or start < 0 or end > len(doc.text):
                print(f"Invalid span in text: '{text}', start: {start}, end: {end}, label: '{label}'")
                continue
            
            # Check if the current span overlaps with any existing span
            if any(s < end and start < e for s, e in spans):
                print(f"Overlapping span detected in text: '{text}' for span ({start}, {end}) with label '{label}'")
                has_overlap = True
                continue  # Skip this overlapping span
            
            try:
                # Try creating a span and handling potential issues
                print("charspan",doc.text[start:end], label)
                print(f"Tokens: {[token.text for token in doc]}")
                span = doc.char_span(start, end, label=label)
                print(span)
                if span is None:
                    # print(f"Warning: Failed to create span for ({start}, {end}) in text: '{text}' with label '{label}'")
                    continue  # Skip invalid span
                ents.append(span)
                spans.append((start, end))
            except Exception as e:
                print(f"Exception encountered: {e} for span ({start}, {end}) in text: '{text}' with label '{label}'")
                continue  # Skip this span if there's an error
            print("---"*10)
        i+=1

        

        if not has_overlap:  # Only add if there are no overlaps
            doc.ents = ents
            db.add(doc)


    db.to_disk("./train.spacy")
    return db

def loadTrainData():
    import json
    from spacy.tokens import DocBin

    file = "json/sample.json"

    # Load training data from JSON
    with open(file, "r", encoding="utf-8") as f:
        training_data = json.load(f)

    db = DocBin()
    i = 0

    for text, annotations in training_data:
        doc = nlp.make_doc(text)
        ents = []
        spans = []  # Keep track of start-end positions to detect overlaps
        has_overlap = False  # Flag to check for overlaps

        if i == 1:
            i += 1  # Skip this iteration
            continue

        for entity in annotations["entities"]:
            # Extract start, end, and label from the entity
            start, end, label = entity[0], entity[1], entity[2]
            substring = text[start:end]

            print(f"Processing Entity: Start: {start}, End: {end}, Label: {label}, Text: '{substring}'")
            
            # Validate span
            if start >= end or start < 0 or end > len(doc.text):
                print(f"Invalid span detected: Start: {start}, End: {end}, Label: {label}")
                continue

            # Check for overlaps
            if any(s < end and start < e for s, e in spans):
                print(f"Overlapping span detected: ({start}, {end}) with Label: {label}")
                has_overlap = True
                continue

            try:
                # Create token-aligned span
                print(f"Creating char_span for '{substring}' with label '{label}'...")
                span = doc.char_span(start, end, label=label, alignment_mode="expand")  # Adjust alignment as needed
                
                if span is None:
                    print(f"Warning: Failed to create span for '{substring}' with label '{label}'")
                    continue

                ents.append(span)
                spans.append((start, end))  # Keep track of processed spans
                print(f"Span added: {span.text} with label {span.label_}")

            except Exception as e:
                print(f"Exception encountered: {e} for span ({start}, {end}) with label '{label}'")
                continue

        i += 1

        # Assign processed entities to the document
        if not has_overlap:  # Add document only if there are no overlaps
            doc.ents = ents
            db.add(doc)

    # Save the processed data to disk
    db.to_disk("./train.spacy")
    print("Training data saved successfully!")
    return db


loadTrainData()
















# Load training data from JSON file
# file = "train_data.json"

# Save the DocBin to disk

