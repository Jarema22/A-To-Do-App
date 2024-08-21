from  functione import get_todos, wraite_todos
import  time

now = time.strftime("%d-%b-%Y %H:%M:%S")
print("It Is", now)
while True:
    user_action = input("Type add, show, complete, edit or exit: ")
    user_action = user_action.strip()
    if  user_action.startswith('add') :
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")
        wraite_todos(filepath="todos.txt", todose_arg=todos)

    elif   user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
    elif user_action.startswith("exit"):
        break
    elif user_action.startswith("edit"):
         try:
            number =  int(user_action[5:])
            number = number-1

            todos = get_todos()
            new_todo = input('Add some new staff: ')
            todos[number] = new_todo + "\n"

            wraite_todos(filepath="todos.txt", todose_arg=todos)
         except ValueError:
             print('Your comende is not valide, you are noob' )
             continue

    elif user_action.startswith("complete") :
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

                massege = f"Todo {todo_to_remove} was removed"
                print(massege)
        except IndexError:
            print('Tere are no item with thise number in Warcraft  3 , you are noob')
            continue
    else:
        print("YOU ARE NOOB!")

print('Arrivederchi!')
