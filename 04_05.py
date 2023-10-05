import re 

# I found over 5k instance with ctrl+f so this 3798 is  bit weird number
# Some IDs and names are duplicates in that 5k number
pattern = r"TIE|surfacemoisture"

fh = open('weather-data.json', 'r')

matches_as_list = re.findall(pattern, fh.read())
print(len(matches_as_list))