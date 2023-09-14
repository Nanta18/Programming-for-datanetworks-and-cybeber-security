input_strings = ["Dog", "Cat", "Moose", "Mouse", "Rhino", "Dodo", "Manatee"]

def is_first_char_m(sana):
    if sana[0].lower() == 'm':
        return 'a' + sana
    else:
        return 'b' + sana 

M_sorted = sorted(input_strings, key=is_first_char_m)
print(M_sorted)
