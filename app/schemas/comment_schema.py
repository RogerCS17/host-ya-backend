from pydantic import BaseModel

class CommentCreate(BaseModel):
    user_id: str
    text: str
