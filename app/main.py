from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import app.crud as crud, app.database as database
from app.schemas import TaskSchema

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

@app.post('/todos/create',response_model=TaskSchema.CreateTask)
def create_task(todo: TaskSchema.CreateTask,db: Session=Depends(get_db)):
    return crud.createTask(db=db,todo=todo)