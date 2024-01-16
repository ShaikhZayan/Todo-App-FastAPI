# Todo App

## Overview

This is a simple Todo App built with FastAPI for the backend and Streamlit for the frontend. The application allows users to add, delete, and edit Todos. The backend is powered by FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Project Structure

- `main.py`: FastAPI backend implementation for managing Todos.
- `streamlit.py`: Streamlit frontend for interacting with the Todo API.
- `create_db.py`: Database configuration using SQLAlchemy for FastAPI.

## Features

- **Add Todo**: Users can add new Todos by entering a title in the Streamlit app.

- **Delete Todo**: Users can delete a Todo by entering its ID in the Streamlit app.

- **Edit Todo**: Users can edit a Todo by entering its ID, a new message, and a new status (True/False) in the Streamlit app.

- **View Todos**: The Streamlit app displays a table of all Todos with their IDs, messages, and statuses.

## Demo Video

[Watch Demo Video](https://streamable.com/stm53c)

## Additional Notes

- The FastAPI app runs on [http://localhost:8000](http://localhost:8000) by default.

- The Streamlit app runs on [http://localhost:8501](http://localhost:8501) by default.

- Make sure the backend is running before using the Streamlit frontend.

