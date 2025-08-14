from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Enable CORS to allow React frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://todo-frontend.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model for a to-do item
class TodoItem(BaseModel):
    id: int
    task: str
    completed: bool = False

# In-memory storage for simplicity
todos: List[TodoItem] = []

@app.get("/todos", response_model=List[TodoItem])
async def get_todos():
    return todos

@app.post("/todos", response_model=TodoItem)
async def create_todo(todo: TodoItem):
    todos.append(todo)
    return todo