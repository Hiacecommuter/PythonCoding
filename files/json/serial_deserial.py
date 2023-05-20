import json   # native module
import requests

# serializing json
data = { "states" : {"NSW" : "Sydney", "VIC" : "Melbourne"} }

with open("data_file.json", "w") as write_file:
  json.dump(date, write_file)
 
json_str = json.dumps(data)
json_str1 = json.dumps(data, indent=4)

# deserializing
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string)    



