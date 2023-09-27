import os
#Prints current working directory
location = os.getcwd()
print("-----------------------------------------------------")
print("Current working directory is " ,location)

#Changes current working directory
new_dir = "C:\\Users\\nanta\\Documents"
os.chdir(new_dir)
print("Directory changed")
location = os.getcwd()

#Prints current working directory to check changes
print("Current working directory is " ,location)
print("-----------------------------------------------------")