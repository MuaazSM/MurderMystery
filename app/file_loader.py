import json

def load_all_mysteries(file_path):
    """Loads the entire list of mysteries from the JSON file."""
    with open(file_path, "r") as f:
        return json.load(f)