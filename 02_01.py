import json

dict_to_jsonify = {
    "iron": 5,
    "silver": 7, 
    "gold": 3, 
    "copper": 4}

# a) Makes a indented version
json_metals = json.dumps(dict_to_jsonify, indent=4)
print(json_metals)

# b) Opens a JSON file named employee.json in read mode. Writes the contents inside "data" dictionary
with open('employee.json', 'r') as file:
    data = json.load(file)

print(data) #prints everything inside data
print(data["name"]) #prints the value of "name" from inside the dictionary