
def count_strings (strings):
    count = 0
    for i in strings:
        if len(i) >= 2 and i[0] == i[-1]:
            count+= 1
    return count 

input_strings = ["Dog", "Cat", "Moose", "B", "Rhino", "odo", "fif"]

answer = count_strings(input_strings)
print(answer)