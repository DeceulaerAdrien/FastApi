from fastapi import FastAPI
from app.routes import TaskRoute

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(
    TaskRoute.router,
    prefix="/tasks",
    tags=["tasks"]
)