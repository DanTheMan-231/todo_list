import os #Imports os module for filepath creation on any system.

# Create a standard directory inside the user's Documents folder
# for a default empty.txt on gui launch.
DEFAULT_DIR = os.path.join(os.path.expanduser("~"), "Documents", "MyTodoApp")
DEFAULT_FILE = os.path.join(DEFAULT_DIR, "default_todos.txt")

# Check that the directory and file exist.
# If not, a new default txt file is created. 
os.makedirs(DEFAULT_DIR, exist_ok=True)

if not os.path.exists(DEFAULT_FILE):
    with open(DEFAULT_FILE, "w") as file:
          file.write("")

def open_file(filepath=DEFAULT_FILE):
        """Read a text file and return the list of 
        to-do items."""
        with open (filepath ,  "r") as file_local:
            todos_local = file_local.readlines()
        return(todos_local)

def write_data(todos_arg ,filepath=DEFAULT_FILE):
        """Write the to-do items list in the text file."""
        with open (filepath, 'w') as file:
            file.writelines(todos_arg)

print(__name__)

if __name__ == "__main__":
      print("Hello")
      print(open_file())