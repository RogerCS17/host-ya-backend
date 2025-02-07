from fastapi import APIRouter, HTTPException
from app.schemas.space_schema import SpaceCreate, SpaceUpdate
from app.services.space_service import create_space, update_space, delete_space, get_all_spaces, get_space_by_id

router = APIRouter(prefix="/spaces", tags=["Spaces"])

@router.post("/")
def create_new_space(space: SpaceCreate):
    return create_space(space)

@router.put("/{space_id}")
def update_existing_space(space_id: str, space: SpaceUpdate):
    return update_space(space_id, space)

@router.delete("/{space_id}")
def remove_space(space_id: str):
    return delete_space(space_id)

@router.get("/")
def get_spaces():
    return get_all_spaces()

@router.get("/{space_id}")
def get_single_space(space_id: str):
    return get_space_by_id(space_id)
