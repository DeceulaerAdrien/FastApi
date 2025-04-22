from sqlalchemy import Column,Integer,String,Boolean,TIMESTAMP,func
from app.database import Base

class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        index=True
    )

    description = Column(
        String,
        nullable=True
    )

    completed = Column(
        Boolean,
        default=False,
        nullable=False
    )

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
