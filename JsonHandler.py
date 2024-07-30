import json

class JsonHandler():
    Json_path = "Data.json"
    try:                                                                    # tries to load the data from the file
        with open(Json_path,"r") as file:
            Json_data = json.load(file)
    except json.decoder.JSONDecodeError:                                    # exception is trown when the file ist empty or invalid
        Json_data = None

    def load_json(self, file_path):                                         # loads a different file
        self.Json_path = file_path
        try:  
            with open(self.Json_path,"r") as newfile:
                self.Json_data = json.load(newfile)
        except json.decoder.JSONDecodeError:
            self.Json_data=None
        return self.Json_data
    
    def get_all_content(self):                                              # returns everything within the json file
        try:
            with open(self.Json_path,"r") as file:
                self.Json_data = json.load(file)
        except json.decoder.JSONDecodeError:
            self.Json_data = None
        return self.Json_data
    
    def get_filtered_content(self, key):                                    # returns only a single attribute from the json file
        if(self.Json_data[key]):                                            # checks if there is such key
            return self.Json_data[key]
        self.errors = f"There is no '{key}' in '{self.Json_path}'"
        return f"There is no '{key}' in '{self.Json_path}'"

    def write_json(self, dict):                                             # writes what comes in dict in the json file
        with open(self.Json_path,"r+") as outputfile:
            json.dump(dict, outputfile)
            try:
                self.Json_data = json.load(outputfile)
            except json.decoder.JSONDecodeError:
                self.Json_data = None
        return self.Json_data