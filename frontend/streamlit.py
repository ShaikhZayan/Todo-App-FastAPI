# streamlit.py

from streamlit_js_eval import streamlit_js_eval
import streamlit as st
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def get_all_todos():
    response = requests.get(BASE_URL)
    response.raise_for_status()
    return response.json()

def get_max_todo_id():
    app = get_all_todos()
    return max([item['id'] for item in app], default=0)

def todo_exists(todo_id):
    app = get_all_todos()
    return any(item['id'] == todo_id for item in app)

def create_todo(title):
    if not title:
        st.warning("Please enter a Todo message.")
        return

    new_id = get_max_todo_id() + 1
    data = {"id": new_id, "message": title, "status": False}
    response = requests.post(f"{BASE_URL}/addTodo", json=data)
    response.raise_for_status()
    streamlit_js_eval(js_expressions="parent.window.location.reload()")
    st.success("Added Todo Successfully")

def delete_todo(todo_id):
    if not todo_id:
        st.warning("Please enter a Todo ID to delete.")
        return

    if not todo_exists(todo_id):
        st.warning(f"Todo with ID {todo_id} does not exist.")
        return

    response = requests.delete(f"{BASE_URL}/delete_todo/{todo_id}")
    response.raise_for_status()
    st.warning("Deleted Todo Successfully!")
    streamlit_js_eval(js_expressions="parent.window.location.reload()")

def update_todo(todo_id, message, status):
    if not todo_id or not message:
        st.warning("Please enter Todo ID and message to update.")
        return

    if not todo_exists(todo_id):
        st.warning(f"Todo with ID {todo_id} does not exist.")
        return

    data = {"id": todo_id, "message": message, "status": status}
    response = requests.put(f"{BASE_URL}/update_todo/{todo_id}", json=data)
    response.raise_for_status()
    streamlit_js_eval(js_expressions="parent.window.location.reload()")
    st.success("Todo Updated Successfully")

def show_todo():
    app = get_all_todos()  # Directly get the list from the API

    st.divider()
    st.markdown("## The Todos List")
    table_content = ""
    for item in app:
        # Convert status to boolean
        status_bool = item['status'] == 'True'
        table_content += f"<tr><td style='border:1px solid black; padding:10px;'>{item['id']}</td><td style='border:1px solid black; padding:10px;'>{item['message']}</td><td style='border:1px solid black; padding:10px;'>{status_bool}</td></tr>"

    st.markdown(f"<table style='border-collapse: collapse; width:100%;'><tr><th>ID</th><th>Todo Message</th><th>Status</th></tr>{table_content}</table>", unsafe_allow_html=True)

if __name__ == "__main__":
    st.title("Todo App")

    title = st.text_input("Enter New Todo", placeholder="Enter A Your Todo")
    if st.button("Add Todo"):
        create_todo(title)

    todo_id = st.number_input("Enter Todo ID to delete", step=1)
    if st.button("Delete Todo"):
        delete_todo(todo_id)

    todo_id_edit = st.number_input("Enter Todo ID to Edit", step=1)
    message_edit = st.text_input("Enter Todo", placeholder="Enter Todo Edited Name")
    status_edit = st.radio("Enter Status", ('False', 'True'))
    status_edit = True if status_edit == 'True' else False
    if st.button("Edit Todo"):
        update_todo(todo_id_edit, message_edit, status_edit)

    show_todo()
