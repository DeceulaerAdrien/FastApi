from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app import database

import app.cruds.TaskCrud as cruds
import app.schemas.TaskSchema as schemas

router = APIRouter()

@router.get('/tasks',response_model=schemas.TaskListResponse)
def read_tasks(db: Session = Depends(database.get_db)):
    tasks = cruds.getTask(db)
    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks found")
    return {"tasks":[schemas.ReadTask.model_validate(task) for task in tasks]}

@router.post('/tasks', response_model=schemas.ReadTask)
def create_task(task: schemas.CreateTask, db: Session = Depends(database.get_db)):
    db_task = cruds.createTask(db, task)
    return db_task