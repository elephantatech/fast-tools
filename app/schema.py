from typing import List
from datetime import date
from pydantic import BaseModel


class CreateTool(BaseModel):
    name: str
    description = str
    acquired_date = date
    condition = str


class Tool(BaseModel):
    id: int
    name: str
    description = str
    acquired_date = date
    condition = str

    class Config:
        orm_mode = True
