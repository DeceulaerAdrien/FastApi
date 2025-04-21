from typing import Union,Optional
from fastapi import FastAPI, Depends
import crud, models, database
from sqlalchemy.orm import Session
from schemas import TaskSchema


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

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/test")
def read_item():
    return {"Le test est concluant"}

@app.post('/todos/create',response_model=TaskSchema.TodoCreate)
def create_task(todo: TaskSchema.TodoCreate,db: Session=Depends(get_db)):
    return crud.createTask(db=db,todo=todo)