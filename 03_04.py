import os

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

check_for_file()
write_new_entries()

#atm empty row is created before first entry this could be fixed by check_for_file returning something if file is empty and write_new_entries could check if that is true and not add \n 