import functions # pip install FreeSimpleGUI
import FreeSimpleGUI as sg
import time
import os

# Load the default blank file on startup.
current_file = functions.DEFAULT_FILE
todos = functions.open_file()

sg.theme("LightGrey3")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=todos, key='todos', 
                      enable_events=True, size=[45,12])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
new_list_button = sg.Button("Create New Todo List")
open_list_button = sg.Button("Open Todo List")

window = sg.Window("My To-Do App", 
                    layout=[[clock],
                            [label],
                            [input_box , add_button],
                            [list_box, edit_button, complete_button],
                            [open_list_button, new_list_button],
                            [exit_button]],
                            font=('Helvetica', 15))

while True:
    event , values = window.read(timeout=215)
    
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S")) 

    if event == 'Add':
        new_todo = ' '.join(values['todo'].split())

        if  new_todo.strip() == "" or new_todo.strip() == "\n":
            sg.popup("Please enter a todo to add.", font=("Helvetica", 12))

        elif any(' '.join(todo.split()).upper() == new_todo.upper() for todo in todos):
            sg.popup(f"{new_todo.title()}\nis already on todo list.", font=("Helvetica", 12))

        else:    
            todos.append(new_todo + '\n')# B2 Ensure we only store clean todos.
            functions.write_data(todos, current_file)
            window['todos'].update(values=todos)
            window["todo"].update(value="")  # B3 - Clear input box
    
    elif event == "Edit":
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_data(todos, current_file)
            window['todos'].update(values=todos)
            window["todo"].update(value="")  # B4 - Clear input box
        except IndexError:
                sg.popup("Please select a todo to edit.", font=("Helvetica", 12))
            
    
    elif event == "Complete":
        try:
            todos_to_complete = values["todos"][0]
            todos.remove(todos_to_complete)
            functions.write_data(todos, current_file)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        except IndexError:
            sg.popup("Please select a todo to complete.", font=("Helvetica", 12))#Only button was clicked.

    elif event == "Create New Todo List":
        new_file = sg.popup_get_file(
            "Create new To-Do list",
            save_as=True,
            default_extension=".txt",
            file_types=(("Text Files", "*.txt"),))
        if new_file:
            current_file = new_file
            todos = []
            functions.write_data(todos, current_file)  # Save empty file
            window["todos"].update(values=todos)  # Refresh UI
    
    elif event == "Open Todo List":
        selected_file = sg.popup_get_file(
            "Select a To-Do list file to open", 
            file_types=(("Text Files", "*.txt"),))
        
        if selected_file and os.path.exists(selected_file):
            current_file = selected_file
            todos = functions.open_file(current_file)
            window["todos"].update(values=todos)  # Refresh UI
    
    elif event == 'todos':
        window['todo'].update(value=values['todos'][0])

window.close()