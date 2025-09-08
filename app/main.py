from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Todo API", description="A simple FastAPI Todo service", version="1.0.0"
)


# Pydantic model -> automatic validation data structure
class Todo(BaseModel):
    id: int
    task: str
    done: bool = False


# In-memory database
todos: List[Todo] = [
    Todo(id=1, task="Learn Docker", done=False),
    Todo(id=2, task="Build FastAPI app", done=True),
]


# First access page message
@app.get("/")
def root():
    return {
        "message": "FastAPI Todo API is running.\n\n You can access in /docs which add this command after URL."
    }


# Get all todos
@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos


# Get a single todo
@app.get("/todos/{todo_id}", response_model=Todo)
def get_single_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Target todo is not found")


# Create a new todo job
@app.post("/todos", response_model=Todo)
def add_todo_job(todo: Todo):
    if any(t.id == todo.id for t in todos):
        raise HTTPException(
            status_code=400, detail=f"Todo with id {todo.id} is already existed."
        )
    todos.append(todo)
    return todo


# Update a todo
@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Target Todo not found")


# Delete a todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    for todo in todos:
        if todo.id == todo_id:
            todos = [todo for todo in todos if todo.id != todo_id]
            return {"message": f"Todo {todo_id} deleted"}
    raise HTTPException(status_code=404, detail="Target Todo not found")
