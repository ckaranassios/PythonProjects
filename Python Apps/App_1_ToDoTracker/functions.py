FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ 
    Opens the default file and reads all lines
    """
    with open(filepath, 'r') as file:
        todo_list_local = file.readlines() 
    return todo_list_local

def write_todos(todo_list, filepath=FILEPATH):
    """
    overwrites document and writes new todo list
    """
    with open(filepath, 'w') as file:
        file.writelines(todo_list)
