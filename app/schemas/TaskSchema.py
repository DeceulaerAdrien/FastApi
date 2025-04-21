from pydantic import BaseModel,Field
from typing import Union,Optional

class TodoCreate(BaseModel):

    name: str =Field(...,title="Nom de la tâche",max_length=50,description="Nom de la tâche a enregistrer en base de donnée")
    description: Optional[str] = Field(None,max_length="300",description="Description la plus complète possible de la tâche")
    completed: bool = Field(description="Status de la tâche actuel")