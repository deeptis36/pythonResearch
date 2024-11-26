import spacy
import json

# Load a blank spaCy model
nlp = spacy.blank("en")
file = "json/corrected_sample.json"
# Load training data
with open(file, "r", encoding="utf-8") as f:
    training_data = json.load(f)

def get_token_span(doc, start, end):
    """
    This function converts character span to token span.
    """
    char_start = start
    char_end = end
    # Get the span of tokens
    token_start, token_end = None, None
    for i, token in enumerate(doc):
        if token_start is None and token.idx <= char_start < token.idx + len(token.text):
            token_start = i
        if token_start is not None and token.idx <= char_end <= token.idx + len(token.text):
            token_end = i + 1  # spaCy is 0-indexed, so we need to include the token at `token_end`
            break
    return (token_start, token_end)

def validate_and_fix_spans(data):
    corrected_data = []
    for text, annotations in data:
        doc = nlp(text)
        valid_entities = []
        for start, end, label in annotations["entities"]:
            # Convert character-based span to token-based span
            token_start, token_end = get_token_span(doc, start, end)
            
            # If we cannot find a valid token span, skip the entity
            if token_start is None or token_end is None:
                print(f"Invalid span: '{text[start:end]}' for label '{label}'")
                print(f"Start: {start}, End: {end}, Text: '{text}'")
                continue
            
            valid_entities.append([token_start, token_end, label])
        
        corrected_data.append([text, {"entities": valid_entities}])
    return corrected_data

# Validate and correct the training data
corrected_training_data = validate_and_fix_spans(training_data)

# Save corrected data back to a new file

with open(file, "w", encoding="utf-8") as f:
    json.dump(corrected_training_data, f, ensure_ascii=False, indent=4)

print("Training data corrected and saved to {file}.")
