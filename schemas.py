from pydantic import BaseModel

from db.models import PackagingType


class CheeseTypeBase(BaseModel):
    name: str
    description: str


class CheeseTypeCreate(CheeseTypeBase):
    pass


class CheeseType(CheeseTypeBase):
    id: int

    class Config:
        orm_mode = True


class CheeseBase(BaseModel):
    title: str
    price: int
    packaging_type: PackagingType


class CheeseCreate(CheeseBase):
    cheese_type_id: int


class Cheese(CheeseBase):
    id: int
    cheese_type: CheeseType

    class Config:
        orm_mode = True
