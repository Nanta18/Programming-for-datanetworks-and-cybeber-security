with open("grades.csv") as new_file:
    for line in new_file:
        line = line.replace("\n", "") #Removes new-line character
        parts = line.split(",") #Values are separated with , so values can be split easilly
        name = parts[0] #First value is the name
        grades = parts[1:] #Everyhting from 2nd value onwards is a grade
        print("Name:", name) #Prints the name as a string
        print("Grades:", grades) #Prints the grades as a list


# B)

# replace() replaces target from where ever it is located even inside a word

# strip() replaces target from in front or behind the string, 
# it can be given value to replace as a parameter here line = line.strip("\n") on line 3 would do the same