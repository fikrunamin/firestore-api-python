from flask import Flask, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)
cred = credentials.Certificate('tesmasjid-firebase-adminsdk-n042m-be8b1fb7eb.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


@app.route('/')
def main():
    return "Firestore API"


@app.route('/insert', methods=['POST'])
def insert():
    id_masjid = request.args.get('id_masjid')
    status = request.args.get('status')
    doc_ref = db.collection(u'masjid').document(id_masjid)
    doc_ref.set({
        u'status': status,
    })
    return 'Berhasil'
