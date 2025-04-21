from typing import Union,Optional
from fastapi import FastAPI, Depends
import crud, database
from sqlalchemy.orm import Session
from schemas import TaskSchema
from models import Taskmodel


app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/test")
def read_item():
    return {"Le test est concluant"}

@app.post('/todos/create',response_model=TaskSchema.TodoCreate)
def create_task(todo: TaskSchema.TodoCreate,db: Session=Depends(get_db)):
    return crud.createTask(db=db,todo=todo)