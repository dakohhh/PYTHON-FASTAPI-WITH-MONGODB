from fastapi import Form
from pydantic import BaseModel




class TaskModel(BaseModel):
    title:str
    description:str





class TaskForm:
    def __init__(self, title:str= Form(),description:str= Form()):

        self.title = title
        self.description = description