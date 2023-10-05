import re

user_input = input("Give a string\n")

def is_alpha_Numeric(user_string):
    patern = "[A-Öa-ö0-9]+"
    return bool(re.fullmatch(patern, user_string))

def is_vowels(user_string):
    patern = "^[aeiouyäöAEIOUYÄÖ]{3,}"
    return bool(re.match(patern, user_string))

def over_hundred(user_string):
    patern = "\d{3,}$"
    return bool(re.match(patern, user_string))

if is_alpha_Numeric(user_input) == True:
    print("a) " + user_input + " is alphanumeric")
else:
    print("a) " + user_input + " is not alphanumeric")

if is_vowels(user_input) == True:
    print("b) " + user_input + " starts with 3 vowels")
else:
    print("b) " + user_input + " doesn't start with 3 vowels")

if over_hundred(user_input) == True:
    print("c) " + user_input + " is 100 or over")
else:
    print("c) " + user_input + " isn't over 100")