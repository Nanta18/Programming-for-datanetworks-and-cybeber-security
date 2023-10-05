import re

patern = "^(0[0-9]|1[0-9]|2[0-4]):[0-5][0-9]:[0-5][0-9]"

user_input = input("Give a time in 24h format hh:mm:ss\n")

is_valid = bool(re.match(patern, user_input))

if is_valid:
    print(user_input + " is a valid time")
else:
    print(user_input + " is not a valid time")