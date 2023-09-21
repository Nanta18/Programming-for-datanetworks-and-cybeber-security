import json

# Opens the json into a dictionary.
# Uses "with" so the file will be closed automatically when program stops using it, similar to "try" in java
with open('weather-data.json') as fh:
    data =json.load(fh)


#Creates a list with all the weather stations inside it
weather_stations = data["weatherStations"]

#Count of times the KUITUVASTE_SUURI_1 shows up in the list
count = 0

# Gets sensorValues from weather-data.json goes through all sensor value lists, 
# inside those lists gets all the name values, if those are equal to KUITUVASTE_SUURI_1 adds +1 to count
for station in weather_stations:
    sensor_values = station.get("sensorValues", [])
    for sensor in sensor_values:
        name = sensor.get("name")
        if name == "KUITUVASTE_SUURI_1":
            count += 1

# Prints the answer
print("KUITUVASTE_SUURI_1 is found ",count, " Times.")