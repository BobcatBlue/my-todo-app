import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"

    # This if-statement prevents an empty to-do from
    # being added if the input_box is cleared
    if todo != "\n":
        todos.append(todo)
        functions.write_todos(todos)
    # Clear the input box once a to-do is added to the list
    st.session_state["new_todo"] = ""

st.title("My Todo App")
st.subheader("This is my to-do app")
st.write("This app is to help you stay organized")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo", label_visibility="hidden",
              placeholder="Add a new to-do...", on_change=add_todo,
              key="new_todo")
