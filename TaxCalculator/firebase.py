import os
import json
import firebase_admin
from firebase_admin import credentials, db
def get_firebase_credentials():
# Try loading from file path (local dev)
    cred_path = os.environ.get("FIREBASE_CREDENTIALS_PATH")
    if cred_path and os.path.exists(cred_path):
        return credentials.Certificate(cred_path)
# Else, try from string (Vercel env var)
    firebase_creds_str = os.environ.get("FIREBASE_CREDENTIALS_JSON")
    if firebase_creds_str:
        firebase_creds_dict = json.loads(firebase_creds_str)
        return credentials.Certificate(firebase_creds_dict)
    raise ValueError("Firebase credentials not found.")
# Initialize only if not already initialized
if not firebase_admin._apps:
    cred = get_firebase_credentials()
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://demo1-29443-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })

database_ref = db.reference()