import functions # pip install FreeSimpleGUI
import FreeSimpleGUI as sg
import time

sg.theme("LightGrey3")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.open_file(), key='todos', 
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
    #print(1, event)
    #print(2, values)
    #print(3, values['todos'])
    if event == 'Add':
        todos = functions.open_file()
        new_todo = values['todo']+ '\n'
        todos.append(new_todo) 
        functions.write_data(todos)
        window['todos'].update(values=todos)
    
    elif event == "Edit":
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            
            todos = functions.open_file()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_data(todos)
            window['todos'].update(values=todos)
        except IndexError:
                sg.popup("Please select a todo to edit.", font=("Helvetica", 12))
            
    
    elif event == "Complete":
        try:
            todos_to_complete = values["todos"][0]
            todos = functions.open_file()
            todos.remove(todos_to_complete)
            functions.write_data(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        except IndexError:
            sg.popup("Please select a todo to complete.", font=("Helvetica", 12))
    
    elif event == 'todos':
        window['todo'].update(value=values['todos'][0])

window.close()