import json

def csv_to_json():
    input_csv = "fruits.csv" #This file will be converted to json
    fruit_prices = create_dict(input_csv) #Creates a python dictionary from csv
    write_json(fruit_prices) #Writes a json-file onto the disk

def write_json(fruit_prices):
    with open("fruit_prices.json", "w") as new_file: #Creates a new file in writing mode
        json.dump(fruit_prices, new_file, indent = 4) #Writes into the new file
   
def create_dict(input_csv):
    with open(input_csv) as new_file:
        fruit_dict = {}
        for line in new_file:
            line = line.replace("\n", "") #Removes new-line character
            parts = line.split(",") #prices are separated with , so prices can be split easilly
            fruit_name = parts[0] #First price is the name
            price = parts[1:] #Seccond line is a price
            fruit_dict[fruit_name] = price #Adds a new key to the dictionary with price as the value
    return fruit_dict #Returns the dictionary created


csv_to_json()