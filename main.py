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
        
