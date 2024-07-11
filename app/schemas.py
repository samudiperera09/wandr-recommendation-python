from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class CategorySchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode: True

class ActivitySchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode: True

class TravellerSchema(BaseModel):
    id: int
    name: str
    country: str
    categories: List[CategorySchema]
    activities: List[ActivitySchema]
    
    class Config:
        orm_mode: True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestTraveller(BaseModel):
    parameter: TravellerSchema = Field(...)

class RequestCategory(BaseModel):
    parameter: CategorySchema = Field(...)

class RequestActivity(BaseModel):
    parameter: ActivitySchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]