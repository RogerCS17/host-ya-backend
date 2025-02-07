from fastapi import APIRouter, HTTPException
from app.schemas.rating_schema import RatingCreate
from app.services.rating_service import add_rating

router = APIRouter(prefix="/ratings", tags=["Ratings"])

@router.post("/{space_id}")
def add_rating_to_space(space_id: str, rating: RatingCreate):
    return add_rating(space_id, rating)
