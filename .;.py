def get_todos(filepath="todos.txt"):
    with open('todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
def wraite_todos(todose_arg, filepath="todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(todose_arg)
import FreeSimpleGUI

window = FreeSimpleGUI.Window("My Todo App", layout=[""])
window.read()
window.close()