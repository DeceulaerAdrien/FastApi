from pydantic import BaseModel, Field
from typing import Optional,List
from datetime import datetime


class CreateTask(BaseModel):
    name: str = Field(
        ...,
        title="Nom de la tâche",
        max_length=50,
        description="Nom de la tâche à enregistrer en base de données"
    )
    description: Optional[str] = Field(
        None,
        title="Description de la tâche",
        max_length=300,
        description="Description la plus complète possible de la tâche"
    )
    completed: bool = Field(
        False,
        title="Statut de la tâche",
        description="Détermine si la tâche est complétée",
        example=False
    )


class ReadTask(BaseModel):
    id: int
    name: str
    description: Optional[str]
    completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class TaskListResponse(BaseModel):
    tasks: List[ReadTask]