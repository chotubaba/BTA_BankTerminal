import json

class FileManager:
    def load_data(self, filename):
        with open(filename, "r")  as f:
            return f.read()

    def save_data(self, filename, data):
        with open(filename, "w") as f:
            f.write(data)

    def read_json(self, json_file_path):
        with open(json_file_path, "r") as f:
            return json.load(f) # returns existing list of dictionaries as python object
        
    def write_json(self, list_of_dicts, json_file_path):
        with open(json_file_path, "w") as f:
            json.dump(list_of_dicts, f)
            
        # TODO:
        # Implement a process that writes a list of dictionaries from list_of_dicts to the `json_file_path` file

    def add_to_json(self, data, json_file_path):
        pass
        # TODO:
        # Implement a process that gets the dictionary in the data variable and adds it to the JSON `json_file_path`

            