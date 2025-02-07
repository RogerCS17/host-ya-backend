from fastapi import APIRouter, HTTPException
from app.schemas.comment_schema import CommentCreate
from app.services.comment_service import add_comment, delete_comment

router = APIRouter(prefix="/comments", tags=["Comments"])

@router.post("/{space_id}")
def add_comment_to_space(space_id: str, comment: CommentCreate):
    return add_comment(space_id, comment)

@router.delete("/{comment_id}")
def remove_comment(comment_id: str):
    return delete_comment(comment_id)
