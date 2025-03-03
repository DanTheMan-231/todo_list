FILEPATH = r"C:\Users\dwhko\OneDrive\Desktop\Python Mega Course Learn Python in 60 Days, Build 20 Apps\todo list\todos.txt"

def open_file(filepath=FILEPATH):
        """Read a text file and return the list of 
        to-do items.
        """
        with open (filepath ,  "r") as file_local:
            todos_local = file_local.readlines()
        return(todos_local)

def write_data(todos_arg ,filepath=FILEPATH):
        """Write the to-do items list in the text file."""
        with open (filepath, 'w') as file:
            file.writelines(todos_arg)

print(__name__)

if __name__ == "__main__":
      print("Hello")
      print(open_file())