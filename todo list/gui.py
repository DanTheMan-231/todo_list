import functions # pip install FreeSimpleGUI
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", 
                    layout=[[label],
                    [input_box , add_button]] ,
                    font=('Helvetica', 15))

while True:
    event , values = window.read() 
    print(event)
    print(values)
    if event == 'Add':
        todos = functions.open_file()
        new_todo = values['todo']+ '\n'
        todos.append(new_todo) 
        functions.write_data(todos)
    elif event == sg.WIN_CLOSED:
        break
window.close()