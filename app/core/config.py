import firebase_admin
from firebase_admin import credentials, auth, firestore
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "../../firebase-credentials.json")

with open(CONFIG_PATH) as f:
    firebase_credentials = json.load(f)

cred = credentials.Certificate(firebase_credentials)
firebase_admin.initialize_app(cred)

db = firestore.client()
firebase_auth = auth
