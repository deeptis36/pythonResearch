import json

def fix_json(json_data):
    """
    Fixes the JSON data by normalizing entities in the 'entities' field.
    It works on both dictionary and list-based JSON structures.
    """
    fixed_list = []
    
    if isinstance(json_data, list):
        for item in json_data:
            try:
                # Assuming item is a list with two elements: text and entities
                text = item[0]
                entities = item[1].get('entities', [])  # Access entities
                fixed_item = {
                    'text': text,
                    'entities': fix_entities(entities)
                }
                fixed_list.append(fixed_item)
            except (IndexError, AttributeError) as e:
                print(f"Error processing item: {item} - {e}")
                continue  # Skip invalid items
        return fixed_list
    elif isinstance(json_data, dict):
        try:
            # If json_data is a dictionary, fix the 'entities' field
            if 'entities' in json_data:
                json_data['entities'] = fix_entities(json_data['entities'])
        except Exception as e:
            print(f"Error processing dictionary: {json_data} - {e}")
        return json_data
    else:
        # Return the data as-is if it's neither a list nor a dictionary
        return json_data

def fix_entities(entities):
    """
    Fixes the entities field, ensuring each entity is a dictionary
    with 'start', 'end', and 'label' keys.
    """
    fixed_entities = []
    for entity in entities:
        try:
            if isinstance(entity, list) and len(entity) == 3:
                # Convert the list format into a dictionary
                fixed_entities.append({
                    'start': entity[0],
                    'end': entity[1],
                    'label': entity[2]
                })
            else:
                print(f"Skipping invalid entity: {entity}")  # Debugging output
        except Exception as e:
            print(f"Error processing entity: {entity} - {e}")
            continue  # Skip invalid entities
    return fixed_entities

def read_and_fix_json(input_file, output_file):
    """
    Reads JSON data from an input file, fixes the structure,
    and writes the corrected data to an output file.
    """
    try:
        # Read the input JSON file
        with open(input_file, 'r') as infile:
            json_data = json.load(infile)
        
        # Fix the JSON data
        fixed_json = fix_json(json_data)
        
        # Write the fixed JSON data back to the output file
        with open(output_file, 'w') as outfile:
            json.dump(fixed_json, outfile, indent=4)
    except Exception as e:
        print(f"Error processing file: {e}")

# Example usage
input_file = 'train_data_fixed.json'  # Replace with your input file path
output_file = 'train_data_fixed_output.json'  # Replace with your output file path

read_and_fix_json(input_file, output_file)
