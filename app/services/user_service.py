from http.client import HTTPException
from firebase_admin import auth
from app.schemas.user_schema import UserRegister
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
