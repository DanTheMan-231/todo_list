
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is now {now}.")

while True:
    user_action = input("Type add , show , edit , complete or exit :")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        
        todos = functions.open_file()
        todos.append(todo + "\n") 

        functions.write_data(todos)
        
    elif user_action.startswith("show"):
        todos = functions.open_file()

        for index , item in enumerate(todos):
            #item = item.strip("\n")
            # comment stuff
            row = (f"{index + 1}-{item.strip("\n")}")
            print(row)

    elif user_action.startswith("edit"):
            try:
                number = int(user_action[5:])
                number -= 1

                todos = functions.open_file()
                
                new_todo = input('Enter new todo :')
                todos[number] = new_todo +"\n"

                functions.write_data(todos)
            except ValueError:
                print("Please enter 'edit' followed by the number you would like to edit.")
                continue            
    
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            
            todos = functions.open_file()
            
            index = number -1 
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_data(todos)
            
            complete_message = f"Task : {todo_to_remove} , has been completed and removed."
            print(complete_message)
        except IndexError:
            print("There is no such number.")
            continue
        except ValueError:
            print("Please enter a number after complete.")
            

    elif user_action.startswith("exit"):
        break

    #else:
        #print("This command is not valid.")

print("Bye!")
print("Another line to say goodbye.")