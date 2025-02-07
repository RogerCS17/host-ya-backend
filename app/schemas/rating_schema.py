from pydantic import BaseModel

class RatingCreate(BaseModel):
    user_id: str
    rating: float
