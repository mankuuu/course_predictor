import pickle
import json

# Function to convert Pickle to JSON
def convert_pkl_to_json(pkl_file, json_file):
    with open(pkl_file, 'rb') as f:
        data = pickle.load(f)  # Load the pickle file
    
    # Save the data to a JSON file
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

# Example: Converting 'priority.pkl' to 'priority.json'

convert_pkl_to_json('priority.pkl', 'priority.json')
convert_pkl_to_json('students.pkl', 'students.json')
convert_pkl_to_json('subjects.pkl', 'subjects.json')
convert_pkl_to_json('code_to_name.pkl', 'code_to_name.json')