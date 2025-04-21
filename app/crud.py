from sqlalchemy.orm import Session
from models import Taskmodel as Taskmodel
from schemas import TaskSchema as schemas

def createTask(db:Session,todo: schemas.TodoCreate):
    db_todo = Taskmodel.Task(
        name=todo.name,
        description=todo.description,
        completed=todo.completed
    )

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo