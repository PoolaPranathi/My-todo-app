import streamlit as sl
import functions

todos = functions.get_todos()

def add_todo():
    todo = sl.session_state['todo'] + '\n'
    todos.append(todo)
    functions.set_todos(todos)

sl.title('My todo App')
sl.subheader('This is my todo list')
sl.write('This app is to improve my productivity')
for index,item in enumerate(todos):
    checkbox = sl.checkbox(item, key = item)
    if checkbox:
        todos.pop(index)
        functions.set_todos(todos)
        del sl.session_state[item]
        sl.rerun()
sl.text_input(label = "", placeholder= "Add new todo...", on_change=add_todo, key = 'todo')
