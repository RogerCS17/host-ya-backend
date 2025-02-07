from http.client import HTTPException
from firebase_admin import auth
from fastapi import HTTPException
from app.schemas.user_schema import UserRegister
from app.schemas.user_schema import UserLogin
from app.core.config import db


def register_user(data: UserRegister):
    try:
        user = auth.create_user(email=data.email, password=data.password)
        user_ref = db.collection("Users").document(user.uid)
        user_ref.set({
            "first_name": data.first_name,
            "last_name": data.last_name,
            "email": data.email,
            "profile_picture": " ",
            "posts": []
        })
        return {"uid": user.uid, "message": "El usuario fue creado correctamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al guardar los datos del usuario: {str(e)}")


def get_all_users():
    try:
        users = db.collection("Users").stream()
        users_list = []
        for user_doc in users:
            user_data = user_doc.to_dict()
            user_data["uid"] = user_doc.id
            users_list.append(user_data)

        return users_list

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener todos los usuarios: {str(e)}")


def login_user(data: UserLogin):
    try:
        user = auth.get_user_by_email(data.email)
        return {"message": "Inicio de sesión exitoso", "user_id": user.uid}
    except Exception:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")


def update_user(user_id: str, data: UserRegister):
    try:
        user_ref = db.collection("Users").document(user_id)
        if not user_ref.get().exists:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        user_ref.update({
            "first_name": data.first_name,
            "last_name": data.last_name,
            "email": data.email,
            "profile_picture": data.profile_picture if data.profile_picture else " "
        })

        return {"message": "Usuario actualizado correctamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar usuario: {str(e)}")

def delete_user(user_id: str):
    try:
        user_ref = db.collection("Users").document(user_id)
        if not user_ref.get().exists:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        # Eliminar de Firestore
        user_ref.delete()

        # Eliminar de Firebase Authentication
        auth.delete_user(user_id)

        return {"message": "Usuario eliminado correctamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar usuario: {str(e)}")
