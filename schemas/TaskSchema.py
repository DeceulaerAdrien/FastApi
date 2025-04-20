from pydantic import BaseModel
from typing import Union,Optional

class TodoCreate(BaseModel):

    name: str
    description: Optional[str] = None
    completed: bool