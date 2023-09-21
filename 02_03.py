import json

with open('todos.json') as file:
    data = json.load(file)

def getKeys():
    unique_keys = set()
    # Goes through all the entries and adds the key into unique_keys set list. 
    # Set only allows unique entries so duplicates don't need to be checked for 
    for item in data:
            unique_keys.update(item.keys())

    print("Keys used in the dictionary are: ", unique_keys)

def getUserIdRange():
    # +/- infinity is used so it will always be larger or smaller than any value in json
    smallest_value = float('inf')
    largest_value = float('-inf')

    # If the user_id is larger than the current value in largest value, it will be replaced
    for item in data:
        user_id = item["userId"]
        if user_id > largest_value:
            largest_value = user_id
    
    # If the user_id is smaller than the current value in smallest value, it will be replaced
    for item in data:
        user_id = item["userId"]
        if user_id < smallest_value:
            smallest_value = user_id    

    print("UserID range is from", smallest_value, "to", largest_value)
    

def getTaskIdRange():
    # +/- infinity is used so it will always be larger or smaller than any value in json
    smallest_value = float('inf')
    largest_value = float('-inf')

    # If the task_Id is larger than the current value in largest value, it will be replaced
    for item in data:
        task_id = item["id"]
        if task_id > largest_value:
            largest_value = task_id
    
    # If the task_id is smaller than the current value in smallest value, it will be replaced
    for item in data:
        task_id = item["id"]
        if task_id < smallest_value:
            smallest_value = task_id    

    print("TaskID range is from", smallest_value, "to", largest_value)
    

def getCompletedTasks():
    # Goes through all the values from "completed" keys, adds +1 if its True
    completedCount = 0
    for item in data:
            isComplete = item.get("completed")
            if isComplete == True:
                completedCount += 1
    print("The number of completed tasks is",completedCount)

def getDelectusTasks():
    #Checks all the titles for the word Delectus. Converts everything to lowercase. Adds +1 if Delectus is found
    searchWord = "Delectus"
    DelectusCount = 0
    for item in data:
            checkDelectus = item.get("title")
            if searchWord.lower() in checkDelectus.lower():
                DelectusCount += 1
    print("Delectus count is", DelectusCount)

print("---------------------------------------------------")
getKeys() 
getUserIdRange()
getTaskIdRange()
getCompletedTasks()
getDelectusTasks()
print("---------------------------------------------------")