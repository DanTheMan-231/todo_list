import functions # pip install FreeSimpleGUI
import FreeSimpleGUI as sg
import time

todos = functions.open_file()# B1 - Reduce File I/O for Better Performance.

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

window = sg.Window("My To-Do App", 
                    layout=[[clock],
                            [label],
                            [input_box , add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                            font=('Helvetica', 15))

while True:
    event , values = window.read(timeout=215)
    
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S")) 

    if event == 'Add':
        new_todo = values['todo']

        if  new_todo.strip() == "" or new_todo.strip() == "\n":
            sg.popup("Please enter a todo to add.", font=("Helvetica", 12))

        else:    
            todos.append(new_todo + '\n')# B2 Ensure we only store clean todos.
            functions.write_data(todos)
            window['todos'].update(values=todos)
    
    elif event == "Edit":
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_data(todos)
            window['todos'].update(values=todos)
            window["todo"].update(value="")  # B3 - Clear input box
        except IndexError:
                sg.popup("Please select a todo to edit.", font=("Helvetica", 12))
            
    
    elif event == "Complete":
        try:
            todos_to_complete = values["todos"][0]
            todos.remove(todos_to_complete)
            functions.write_data(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        except IndexError:
            sg.popup("Please select a todo to complete.", font=("Helvetica", 12))#Only button was clicked.
    
    elif event == 'todos':
        window['todo'].update(value=values['todos'][0])

window.close()