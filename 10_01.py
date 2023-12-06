import os
import random


#WIP
#TODO
#Create 5-10 empty files with randomized names
#Associate an index to every file, either list or dictionary
#Write a string to every file: This file's index is: <index>
#Read the contents and write it to the screen
#remove the files


def choose_amount_of_files ():
    list_of_names = []
    #Generates a random number between 5 and 10
    amount_of_files = random.randint(5,10)
    print("Files to be generated:" , amount_of_files)


    
    #for x in range(amount_of_files):
     #   list_of_names += [str(generate_random_string)]
        #print(list_of_names[x])
    

    #put them into a dictionary here

    #return the dictionary here
    return 0



#file_details = choose_files()

'''
def check_for_file(): #If file exists, does nothing if not creates an empty file
    if os.path.isfile("diary.txt"): 
        pass
    else:
        with open('diary.txt', 'w') as f:
            pass
            
def write_new_entries(): 
    with open('diary.txt', 'r+') as f: #opens  the diary as f and with read and append permissions
        print("Earlier entries:")
        data = f.read() #reads the file into a string
        print(data)
        new_entry = input("\n" + "New diary entry:") #takes user input
        f.writelines("\n" + new_entry) #writes user input into a file
        print("\n" + "Diary saved" + "\n")
'''

choose_amount_of_files()