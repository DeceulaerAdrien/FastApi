from sqlalchemy.orm import Session
from app.models import Taskmodel
from app.schemas import TaskSchema

def createTask(db:Session,todo: TaskSchema.CreateTask):
    db_todo = Taskmodel.Task(
        name=todo.name,
        description=todo.description,
        completed=todo.completed
    )

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def readAllTask():
    return None