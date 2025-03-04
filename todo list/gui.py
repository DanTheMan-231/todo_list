import functions # pip install FreeSimpleGUI
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText("Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[label],[input_box , add_button]])
window.read()
window.close()