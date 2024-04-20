from fastapi import FastAPI, HTTPException
from typing import List
from model import Todo

app = FastAPI()

# Temporary in-memory storage for todos

todos = [
    Todo(id=1,title="flyhigh",description="the alchemist",completed=False),
    Todo(id=2,title="Wolf",description="Tyler the creator",completed=True),
    Todo(id=3,title="mm Food",description="MF DOOM",completed=False)
]


# Counter for generating unique todo IDs
todo_id_counter = 0


@app.post("/todos/", response_model=Todo)    # the thing in the quotation marks is a route e.g "/todos/" is the route 
async def create_todo(todo: Todo):
    global todo_id_counter
    todo_id_counter += 1
    todo.id = todo_id_counter
    todos.append(todo)
    return todo

detail = "Todo not found"
@app.get("/todos/{todo_id}", response_model=Todo)
async def read_todos(todo_id: int):
    for existing_todo in todos:
        if existing_todo.id == todo_id:
            return existing_todo
    raise HTTPException(status_code=404, detail = detail)

@app.get("/todos/", response_model=list[Todo])
async def read_todos():
    return todos


@app.get("/todos/{todo_parameter}//", response_model=Todo)
async def read_strings(todo_parameter: str):
    for existing_todo in todos:
        if existing_todo.title == todo_parameter or existing_todo.description == todo_parameter:
            return existing_todo
    raise HTTPException(status_code=404, detail=detail)    


@app.get("/todos//{todo_completed}//", response_model=Todo)
async def read_todos(todo_completed: bool):
    for existing_todos1 in todos:
        if existing_todos1.completed == todo_completed:
            return existing_todos1
    raise HTTPException(status_code=404, detail=detail)






@app.put("/todos/{todo_id}/", response_model=Todo)
async def update_todo(todo_id: int, todo: Todo):
    for index, existing_todo in enumerate(todos):
        if existing_todo.id == todo_id:
            todos[index] = todo
            return todo
    raise HTTPException(status_code=404, detail=detail)

@app.delete("/todos/{todo_id}/", response_model=Todo)
async def delete_todo(todo_id: int):
    for index, existing_todo in enumerate(todos):
        if existing_todo.id == todo_id:
            deleted_todo = todos.pop(index)
            return deleted_todo
    raise HTTPException(status_code=404, detail=detail)

# based on what we've done, do the CRUD of a user, count the number of all users, then count for each of the different individual user types e.g student, teacher