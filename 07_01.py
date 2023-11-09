import requests
import urllib.parse
import json

api_key = "uvAzasIo6oVxHHwgrFH4HHg93gjZKK4U"
url = "http://www.mapquestapi.com/directions/v2/route"

orig = "Turku"
destination = "Helsinki"

url = url + "?" + urllib.parse.urlencode({"key":api_key,"from":orig,"to":destination})
print("Request URL:", url)
data = requests.get(url)
json_data = data.json()

#print(json.dumps(json_data, indent=4))

travel_distance = json_data['route']['distance'] #gets distance from json
travel_time = json_data['route']['time'] # Gets travel time from json
time_as_hours = travel_time / 3600 # Turns secconds into hours
rounded_hours = round(time_as_hours, 1) # Rounds the long value to x.x format

print("--------------------------------------------------------------------")
for entry in json_data['route']['legs'][0]['maneuvers']:  #data is inside legs is inside route and this goes trough all of them starting from 0
    print(entry["narrative"]) # Narrative is printed to user

print("--------------------------------------------------------------------")
print("Distance between", orig ,"and", destination ,"is", travel_distance, "km.")
print("Travel time is", rounded_hours, "hours")
print("--------------------------------------------------------------------")
