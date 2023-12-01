import argparse
import os

parser = argparse.ArgumentParser(
    description='Creates a file to collect user strings, if using -i appends to the existing file instead')

parser.add_argument('filename')
parser.add_argument('user_string', type=str, help="String from user inside quotes")
parser.add_argument('-i', '--input', action='store_true', help='Appends to the end of file instead of overwriting it')

args = parser.parse_args()

filename = args.filename
user_string = args.user_string
append_to_file = args.input

def file_editor(filename): 
    check_for_file(filename) #checks for a file and creastes it if missing
    write_new_entries(filename, append_to_file, user_string) #Writes into the user specified file

def check_for_file(filename): #If file exists, does nothing if not creates an empty file
    if os.path.isfile(filename): 
        pass
    else:
        with open(filename, 'w') as f:
            pass
     
def write_new_entries(filename, append_to_file, user_string,): 
    if append_to_file == True: # Runs if -i or --input were user
        with open(filename, 'a') as f: # Opens the file with append permissions
            f.writelines("\n" + user_string) #writes user input into a file
    elif append_to_file == False: # Runs if -i or --input were not used
        with open(filename, 'w') as f: # Opens the file with write permissions
            f.writelines("Beginning of input stash:") # Writes this to the start of the file

file_editor(filename) #calls fo the file editor function