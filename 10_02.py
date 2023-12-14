import os

# Colors are used to show difference between a folder and a file
class Color:
    GREEN = "\033[92m" # File
    BLUE = "\033[94m" # Folder
    RESET = "\033[0m" # Reset to white

# Just adds the color to prints but doesn't change anything else
def print_colored_text(text, color):
    colored_text = f"{color}{text}{Color.RESET}"
    print(colored_text)

def list_directory_contents(directory_path="."): # Uses current working directory as the filepath so it can be used in any folder via commandline

    full_path = os.path.join(os.getcwd(), directory_path) # Creates a full path of current working directory

    # List all files and directories inside the specified directory
    with os.scandir(directory_path) as entries:
        for entry in entries:
            # Check if the entry is a file
            if entry.is_file(): 
                # Filter out files containing 'sikrit' in their name
                if 'sikrit' not in entry.name:
                    print_colored_text(entry.name, Color.GREEN) # Is a file and prints as Green
            elif entry.is_dir():
                print_colored_text(f"{entry.name}", Color.BLUE) # Is a folder and prints as Blue

list_directory_contents()
