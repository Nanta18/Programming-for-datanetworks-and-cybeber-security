def read_fruits():
    with open("fruits.csv") as new_file:
        fruit_dict = {}
        for line in new_file:
            line = line.replace("\n", "") #Removes new-line character
            parts = line.split(",") #Values are separated with , so values can be split easilly
            fruit_name = parts[0] #First value is the name
            value = parts[1:] #Seccond line is a value
            fruit_dict[fruit_name] = value #Adds a new entry to the dictionary with a numerical value

        print("--------------------------------------------------------------------")
        print(fruit_dict) 
        print("--------------------------------------------------------------------")

read_fruits() #Calls the function