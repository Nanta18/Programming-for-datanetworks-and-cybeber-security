def count_strings (strings):
    count = 0
    for i in strings:
        #checks if the word is longer than 2 characters and if first and last characters match. Adds +1 to count if both are true.
        if len(i) >= 2 and i[0] == i[-1]:
            count+= 1
    return count 

input_strings = ["Dog", "Cat", "Moose", "B", "Rhino", "odo", "fif"]

answer = count_strings(input_strings)
print(answer)