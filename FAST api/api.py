from fastapi import FastAPI
from pydantic import BaseModel
class Todo(BaseModel):
    id: int
    item: str

app = FastAPI()

todos = []

@app.get("/")
async def root():
    return { "message": "Hello World"}


@app.get("/todos")
async def get_todos():
    return {"todos": todos}


@app.post("/todos")
async def create_todo(todo: Todo):
    todos.append(todo)
    return {"massage": "todo is added" }
    


@app.get("/todos/{id}")
async def get_todo(id: int):
    for todo in todos:
        if todo.id == id:
            return {"todo": todo}
    return {"massage": "todo not found"}




@app.delete("/todos/{id}")
async def delete_todo(id: int):
    for todo in todos:
        if todo.id == id:
            todos.remove(todo)
            return {"massage": "todo is deleted"}
    return {"massage": "todo not found"}




@app.put("/todos/{id}")
async def update_todo(id: int, newtodo: Todo):
    for todo in todos:
        if todo.id == id:
            todo.item = newtodo.item
            return {"todo" : todos}
    return {"massage": "todo not found"}


