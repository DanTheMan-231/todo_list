import functions # pip install FreeSimpleGUI
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.open_file(), key='todos', 
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App", 
                    layout=[[label],
                    [input_box , add_button],[list_box, edit_button]],
                    font=('Helvetica', 15))

while True:
    event , values = window.read() 
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    if event == 'Add':
        todos = functions.open_file()
        new_todo = values['todo']+ '\n'
        todos.append(new_todo) 
        functions.write_data(todos)
        window['todos'].update(values=todos)
    
    elif event == "Edit":
        todo_to_edit = values['todos'][0]
        new_todo = values['todo']
        
        todos = functions.open_file()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo
        functions.write_data(todos)
        window['todos'].update(values=todos)
    elif event == 'todos':
        window['todo'].update(value=values['todos'][0])

    elif event == sg.WIN_CLOSED:
        break

window.close()