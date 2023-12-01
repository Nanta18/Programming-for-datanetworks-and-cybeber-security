import requests
import argparse
import json

parser = argparse.ArgumentParser(
    description='Gets information a ship based on MMSI given as an argument')

parser.add_argument('ship_id', type=int, help="MMSI of the ship")
args = parser.parse_args()

id_from_user = args.ship_id # Turns the MMSI from user into a variable

url = "https://meri.digitraffic.fi/api/ais/v1/vessels/"

id_from_user = str(id_from_user) # Turns the id into str from int

url = url + id_from_user # Creates the final url

data = requests.get(url) # Gets the data from url
json_data = data.json() # turns the data text into json

readable_json = json.dumps(json_data, indent=2)  # Converts the JSON response to a readable format

print(readable_json) # Prints the json into the console
