from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from db.engine import SessionLocal

app = FastAPI()


def get_db() -> Session:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root() -> dict:
    return {"message": "Hello World"}


@app.get("/cheese_types/", response_model=list[schemas.CheeseType])
def read_cheese_types(db: Session = Depends(get_db)):
    return crud.get_all_cheese_types(db=db)


@app.post("/cheese_types/", response_model=schemas.CheeseType)
def create_cheese_type(
        cheese_type: schemas.CheeseTypeCreate,
        db: Session = Depends(get_db)
):
    db_cheese_type = crud.get_cheese_type_by_name(db=db, name=cheese_type.name)

    if db_cheese_type is not None:
        raise HTTPException(
            status_code=400,
            detail="Cheese type with this name already exists"
        )

    return crud.create_cheese_type(db=db, cheese_type=cheese_type)
