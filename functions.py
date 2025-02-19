def get_todos(filepath = "todos.txt"):
    """ Read the content in the todo.txt file """
    with open(filepath, 'r') as file:
        content = file.readlines()
    return content

def set_todos(todos, filepath = "todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos)

