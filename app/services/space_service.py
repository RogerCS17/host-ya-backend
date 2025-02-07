from firebase_admin import firestore
from app.schemas.space_schema import SpaceCreate, SpaceUpdate
from fastapi import HTTPException

db = firestore.client()

def create_space(space: SpaceCreate):
    space_ref = db.collection("Spaces").document()
    space_ref.set(space.dict())
    return {"id": space_ref.id, "message": "Espacio creado exitosamente"}

def update_space(space_id: str, space: SpaceUpdate):
    space_ref = db.collection("Spaces").document(space_id)
    if not space_ref.get().exists:
        raise HTTPException(status_code=404, detail="Espacio no encontrado")
    space_ref.update(space.dict(exclude_unset=True))
    return {"message": "Espacio actualizado correctamente"}

def delete_space(space_id: str):
    space_ref = db.collection("Spaces").document(space_id)
    if not space_ref.get().exists:
        raise HTTPException(status_code=404, detail="Espacio no encontrado")
    space_ref.delete()
    return {"message": "Espacio eliminado correctamente"}

def get_all_spaces():
    spaces = db.collection("Spaces").stream()
    return [doc.to_dict() for doc in spaces]

def get_space_by_id(space_id: str):
    space_ref = db.collection("Spaces").document(space_id)
    space_doc = space_ref.get()
    if not space_doc.exists:
        raise HTTPException(status_code=404, detail="Espacio no encontrado")
    return space_doc.to_dict()
