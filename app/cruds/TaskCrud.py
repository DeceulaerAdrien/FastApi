from sqlalchemy.orm import Session
from app.models.Taskmodel import TaskModel
from app.schemas import TaskSchema

def createTask(db:Session,task: TaskSchema.CreateTask):
    db_task = TaskModel(
        name=task.name,
        description=task.description,
        completed=task.completed
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def getTask(db:Session):
    return db.query(TaskModel).all()