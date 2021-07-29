from datetime import date
from sqlalchemy.orm import Session
from . import models, schema


def get_tool(db: Session, tool_id: int):
    return db.query(models.Tool).filter(models.Tool.id == tool_id).first()


def get_tools(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tool).offset(skip).limit(limit).all()


def get_tools_by_name(db: Session, name: str):
    return db.query(models.Tool).filter(models.Tool.name == name).all()


def get_tools_by_condition(db: Session, condition: str):
    return db.query(models.Tool).filter(models.Tool.condition == condition).all()


def get_tools_by_date_aquired(db: Session, aquired_date: date):
    return db.query(models.Tool).filter(models.Tool.acquired_date == aquired_date).all()


def add_tool(db: Session, tool: schema.CreateTool):
    db_tool = models.Tool(
        name=tool.name,
        description=tool.description,
        acquired_date=tool.acquired_date,
        condition=tool.condition,
    )

    db.add(db_tool)
    db.commit()
    db.refresh(db_tool)
    return db_tool


def remove_tool(db: Session, tool_id: int) -> dict:
    affected_rows = db.query(models.Tool).filter(models.Tool.id == tool_id).delete()

    if affected_rows == 0:
        raise Exception(f"Tool ID:{tool_id} not found in database")
    else:
        db.commit()

    return {"deleted": affected_rows}
