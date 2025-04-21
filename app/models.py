from sqlalchemy import Column,Integer,String,Boolean
from database import Base

class Task(Base):
    __tablename__="Tasks"

    id= Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True)
    description=Column(String,nullable=True)
    completed=Column(Boolean,default=False)