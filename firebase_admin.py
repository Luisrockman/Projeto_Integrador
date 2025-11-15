import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("C:\Usarios\luish\Downloads\projeto-integrador-a4066-firebase-adminsdk-fbsvc-d7c7ccbfea.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
