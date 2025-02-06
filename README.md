# Host-YA - Backend con FastAPI y Firebase

Host-YA es una red social enfocada en jóvenes que buscan rentar espacios como departamentos, casas de playa u otros ambientes de recreación con la particularidad de que las reservas se realizan el mismo día.

Este repositorio contiene el backend de Host-YA desarrollado con **FastAPI** y **Firebase**.

---

## Requisitos

- **Python 3.13.1**
- Cuenta de Firebase con autenticación habilitada
- Firestore configurado
- Dependencias listadas en `requirements.txt`

---

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/host-ya-backend.git
cd host-ya-backend
```

### 2. Crear un entorno virtual (opcional, pero recomendado)
```bash
python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate    # En Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Firebase
Coloca tu archivo `firebase-credentials.json` en la carpeta principal del proyecto. Este archivo contiene las credenciales de Firebase necesarias para la autenticación y base de datos.

---

## Estructura del Proyecto

```
Host-YA/
│
├── app/                           # Paquete principal de la aplicación
│   ├── __init__.py                # Indica que esta carpeta es un paquete
│   ├── core/                      # Configuración y servicios básicos
│   │   ├── __init__.py
│   │   ├── config.py              # Configuración de Firebase y otras
│   ├── routes/                    # Rutas de FastAPI
│   │   ├── __init__.py
│   │   └── user_route.py          # Rutas para usuarios (registro, login, etc.)
│   ├── schemas/                   # Esquemas de datos para validación con Pydantic
│   │   ├── __init__.py
│   │   └── user_schema.py         # Esquema para registro y datos de usuarios
│   ├── services/                  # Lógica de negocio
│   │   ├── __init__.py
│   │   └── user_service.py        # Registro, obtención y manejo de usuarios
│   ├── main.py                    # Archivo principal para iniciar la aplicación FastAPI
│
├── requirements.txt               # Librerías necesarias para el proyecto
├── .gitignore                     # Archivos o carpetas a ignorar por git
├── firebase-credentials.json      # Credenciales de Firebase (NO compartir)
└── README.md
```

---

## Uso

### Ejecutar el servidor de FastAPI
```bash
uvicorn app.main:app --reload
```

El servidor iniciará en `http://127.0.0.1:8000/`

### Documentación con Swagger
FastAPI proporciona documentación automática en:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Endpoints Principales

### 1. Registro de Usuarios
**POST** `/users/register`
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "johndoe@example.com",
  "password": "securepassword"
}
```

### 2. Obtener Todos los Usuarios
**GET** `/users/all`
```json
{
  "users": [
    {
      "uid": "P3kL1A2BXY78",
      "first_name": "Gepeto",
      "last_name": "Black",
      "email": "gepetoblack@gmail.com",
      "profile_picture": " ",
      "posts": []
    }
  ]
}
```

