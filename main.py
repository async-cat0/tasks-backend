from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="My Fast API App", version="1.0.0")

class Task(BaseModel):
    id:int
    title:str
    description: Optional[str] = None
    done:bool = False

tasks: List[Task] = []

# task creator
@app.post('/tasks/',status_code=201)
def create_tasks(task: Task):
    tasks.append(task)
    print(tasks)              
    return 'Задача создана!' # or return 'Task created!'

# output of all tasks
@app.get('/tasks/')
def get_all_tasks():
    return tasks

# tasks output by ID
@app.get('/tasks/{task_id}')
def get_tasks_by_id(task_id:int):
    for item in tasks:
        if item['id'] == task_id:
            return item
        
# IN DEVELOPMENT

# @app.put('/tasks/{tasks_id}')
# def update_by_id(tasks_id:int,task: Task):
#     for item in tasks:
#         if item['id'] == tasks_id:



# delete task by id
@app.delete('/task/{task_id}')
def task_del_by_id(task_id:int):
    for index,item in enumerate(tasks):
        if item.id == task_id:
            tasks.pop(index)
            return { "message": "task delete" }
    return { "error": "task not found"}