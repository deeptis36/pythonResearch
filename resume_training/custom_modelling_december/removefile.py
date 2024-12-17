import json
import os

# Path to the JSON file
file_path = 'json/file_removal_list.json'

# Read the JSON file
with open(file_path, 'r') as file:
    file_names = json.load(file)
# print(file_names)
for file_name in file_names:
    try:
        file = f"{file_name}"        
        os.remove(file_name)  # Delete the file
        print(f"Deleted: {file_name}")
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except Exception as e:
        print(f"Error deleting {file_name}: {e}")