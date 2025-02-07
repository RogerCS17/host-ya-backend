from firebase_admin import firestore
from app.schemas.rating_schema import RatingCreate
from fastapi import HTTPException

db = firestore.client()

def add_rating(space_id: str, rating: RatingCreate):
    rating_ref = db.collection("Spaces").document(space_id).collection("Ratings").document()
    rating_ref.set(rating.dict())
    return {"id": rating_ref.id, "message": "Valoración agregada correctamente"}
