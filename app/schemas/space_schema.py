from pydantic import BaseModel
from typing import Optional

class SpaceCreate(BaseModel):
    title: str
    description: str
    price: float
    location: str
    owner_id: str
    images: list[str]

class SpaceUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    price: Optional[float]
    location: Optional[str]
    images: Optional[list[str]]
