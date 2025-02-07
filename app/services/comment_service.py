from firebase_admin import firestore
from app.schemas.comment_schema import CommentCreate
from fastapi import HTTPException

db = firestore.client()

def add_comment(space_id: str, comment: CommentCreate):
    comment_ref = db.collection("Spaces").document(space_id).collection("Comments").document()
    comment_ref.set(comment.dict())
    return {"id": comment_ref.id, "message": "Comentario agregado correctamente"}

def delete_comment(comment_id: str):
    comment_ref = db.collection_group("Comments").where("id", "==", comment_id).get()
    if not comment_ref:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    comment_ref[0].reference.delete()
    return {"message": "Comentario eliminado correctamente"}
