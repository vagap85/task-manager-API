from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from fastapi.middleware.cors import CORSMiddleware  # Импорт здесь

from .schemas.task import Task, TaskCreate, TaskUpdate
from .crud.task import (
    create_task, get_tasks, get_task, update_task, delete_task
)
from .database import engine, get_db, Base
from .models.task import TaskStatus

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Task Manager API",
    description="Simple REST API for task management",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React порт
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все HTTP методы
    allow_headers=["*"],  # Разрешить все заголовки
)

# Теперь эндпоинты
@app.post("/tasks/", response_model=Task)
def create_task_endpoint(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db=db, task=task)

@app.get("/tasks/", response_model=List[Task])
def read_tasks_endpoint(
    status: Optional[TaskStatus] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    tasks = get_tasks(db, skip=skip, limit=limit, status=status)
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def read_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    db_task = get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task_endpoint(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    db_task = update_task(db, task_id=task_id, task_update=task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    success = delete_task(db, task_id=task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}