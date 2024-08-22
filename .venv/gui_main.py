from tkinter.ttk import Label

import functione
import FreeSimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo" )
add_botton = sg.Button("Add todo")

window = sg.Window("My Todo App", layout=[[label, input_box, add_botton] ])
window.read()
window.close()