import re 

# I don't know if this was supposed to catch also those with TIE in the end or  middle
# now it only catches TIE_1 and TIE_2 alongside with surfacemoisture1 and surfacemoisture2
# KASTEPISTE_ERO_TIE for example is not caught
# short format name of TIE_1 would be TIE1 that is not caught as a duplicate
pattern = r"TIE|surfacemoisture"

fh = open('weather-data.json', 'r')

matches_as_list = re.findall(pattern, fh.read())
print(len(matches_as_list))