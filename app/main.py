from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK

from . import crud, models, schema
from .database import SessionLocal, engine
from .version import __version__
from app import version

models.Base.metadata.create_all(bind=engine)

app = FastAPI(version=__version__)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health/")
def health():
    return JSONResponse(
        content={"status": "ok", "version": __version__}, status_code=HTTP_200_OK
    )


@app.get("/tools/", response_model=List[schema.Tool])
def get_tools(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_tools = crud.get_tools(db=db, skip=skip, limit=limit)
    return db_tools


@app.post("/tools/", response_model=schema.Tool)
def create_tool(tool: schema.CreateTool, db: Session = Depends(get_db)):
    db_tool = crud.get_tools_by_name(db=db, name=tool.name)
    print(db_tool)
    if len(db_tool) != 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Tool already in database"
        )
    return crud.add_tool(db=db, tool=tool)


@app.delete("/tools/", response_model=schema.Tool)
def delete_tool(tool_id: int, db: Session = Depends(get_db)):
    db_tool = crud.get_tool(db, tool_id=tool_id)
    if db_tool is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tool not found"
        )
    else:
        crud.remove_tool(db=db, tool_id=tool_id)
    return db_tool[0]
