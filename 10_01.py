import os
import random

folder_path = "C:\\Users\\nanta\\Downloads\\testprogram"

# Defines amout of files and returns the dictionary of filenames and indexes 
def choose_amount_of_files():
    list_of_files = {} # Creates an empty dictionary
    # Generates a random number between 5 and 10
    amount_of_files = random.randint(5, 10)
    print("Files to be generated:", amount_of_files)

    # Generates names of all the files
    for i in range(1, amount_of_files + 1):
        file_name = generate_random_name()
        list_of_files[file_name] = i

    #Returns a dictionary containing filenames and indexes
    return list_of_files

# Generates random strings with only captialized leters
def generate_random_name(): 
    name = ""
    for _ in range(5):
        random_number_for_name = random.randint(1, 26) # Gives random number to be used in choosing a character
        name += chr(ord('A') + random_number_for_name - 1)
    return name

# Creates the files, but that should be quite clear from the name of the function
def create_files(files_list, folder_path):

    for file_name, index in files_list.items():
        file_path = os.path.join(folder_path, file_name) # Joins the filepath and the filename into one path
        with open(file_path, 'w') as file: # Opens the file with write permissions
            file.write(f"This file's index is: {index}") # Writes into the file

# Prints one by one contents of the all created files
def read_and_print_contents(files_list, folder_path): 
    for file_name, index in files_list.items():
        file_path = os.path.join(folder_path, file_name) # Joins the filepath and the filename into one path
        with open(file_path, 'r') as file: # Opens the file with read permissions
            contents = file.read()
            print(f"File {file_name} contents: {contents}")

# Deletes all the files we just spent sweat, blood and tears creating
def remove_files(files_list, folder_path):
    for file_name in files_list.keys():
        file_path = os.path.join(folder_path, file_name) # Joins the filepath and the filename into one path
        os.remove(file_path) # Kills the poor file

files_list = choose_amount_of_files()
create_files(files_list, folder_path)
read_and_print_contents(files_list, folder_path)
remove_files(files_list, folder_path)