from fastapi import APIRouter
from typing import List
from app.schemas import RecommendationRequest, RecommendationResponse
from app.utils.recommend import recommend_places

router = APIRouter()

@router.post("/recommendations", response_model=List[RecommendationResponse])
def get_recommendations(request: RecommendationRequest):
    user = request.user
    places = request.places
    recommendations = recommend_places(user.categories, user.activities, places)
    return recommendations
