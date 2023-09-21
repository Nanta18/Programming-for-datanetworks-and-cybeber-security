import json

with open('todos.json') as file:
    todos_data = json.load(file)

with open('users.json') as file:
    users_data = json.load(file)

# Empty dictionary is created for the values
user_tasks = {}

# Goes through all the users in the users_fata json
for item in users_data:
        get_id_users = item.get("id")
        get_name = item.get("name")

        # Goes trough all the tasks in the todos_data
        for task_item in todos_data:
            get_id_todos = task_item.get("userId")
            get_completed = task_item.get("completed")
            # Checks if tasks are done and and also match the user whose tasks we are counting atm
            # setdefault creates the key if it doesn't exist, if it does +1 is added
            if get_completed == True and get_id_users == get_id_todos:
                user_tasks.setdefault(get_name, 0)
                user_tasks[get_name] += 1  
               
# user_tasks.items() turns the dictionary to list of key-value pairs.  
# lambda returns the seccond value from the pair to be used as a sorting key. Sorting is reversed.           
sorted_user_tasks = sorted(user_tasks.items(), key=lambda item: item[1], reverse=True)
print(sorted_user_tasks)


