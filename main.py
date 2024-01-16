from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from backend.database import SessionLocal
import logging
import model.models as models
import logging
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = SessionLocal()

class OurBaseModel(BaseModel):
    class Config:
        from_attributes = True

class Todo(OurBaseModel):
    id: int
    message: str
    status: bool

logging.basicConfig(filename="fastapi_logs.log", level=logging.INFO)

@app.get("/logs")
def get_logs():
    with open("fastapi_logs.log", "r") as log_file:
        logs = log_file.read()
    return {"logs": logs}

@app.get('/', response_model=list[Todo], status_code=status.HTTP_200_OK)
def getAll_Todo():
    getAllTodo = db.query(models.Todo).all()
    return getAllTodo

@app.get('/getbyid/{todo_id}', response_model=Todo, status_code=status.HTTP_200_OK)
def get_Single_Todo(todo_id: int):
    get_Todos = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if get_Todos is not None:
        return get_Todos
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

@app.post('/addTodo', response_model=Todo, status_code=status.HTTP_201_CREATED)
def addTodo(todo: Todo):
    newTodo = models.Todo(id=todo.id, message=todo.message,status=todo.status)
    addTodo = db.query(models.Todo).filter(models.Todo.id == todo.id).first()
    if addTodo is not None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Todo already exists")
    db.add(newTodo)
    db.commit()
    return newTodo

@app.put('/update_todo/{todo_id}', response_model=Todo, status_code=status.HTTP_202_ACCEPTED)
def update_Todo(todo_id:int, todo: Todo):
    find_Todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if find_Todo is not None:
        find_Todo.id = todo.id
        find_Todo.message = todo.message
        find_Todo.status = todo.status
        db.commit()
        return find_Todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo not found")

@app.delete('/delete_todo/{todo_id}', response_model=Todo, status_code=200)
def delete_Todo(todo_id: int):
    find_Todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if find_Todo is not None:
        db.delete(find_Todo)
        db.commit()
        return find_Todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo not found")
