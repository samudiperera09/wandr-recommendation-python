from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    categories: List[str]
    activities: List[str]

class Place(BaseModel):
    id: int
    name: str
    categories: List[str]
    activities: List[str]

class RecommendationRequest(BaseModel):
    user: User
    places: List[Place]

class RecommendationResponse(BaseModel):
    placeId: int
    placeName: str
    similarity: float

