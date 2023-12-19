from pydantic import BaseModel


class CheeseTypeBase(BaseModel):
    name: str
    description: str


class CheeseTypeCreate(CheeseTypeBase):
    pass


class CheeseType(CheeseTypeBase):
    id: int

    class Config:
        orm_mode = True
