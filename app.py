import streamlit as st
from utils.firebase import init_firebase
from firebase_admin import firestore

# Initialize the Firebase Admin SDK
init_firebase()

# Get a reference to the Firestore database
clients_ref = firestore.client().collection('clients')

data = []

for doc in clients_ref.stream():
    print('{} => {}'.format(doc.id, doc.to_dict()))

# @st.cache_data


def on_snapshot(_doc_snapshot, changes, read_time):
    for doc in _doc_snapshot:
        client_data = doc.to_dict()
        row = [
            client_data['name'],
            # client_data['inviteEmails'],
        ]
        data.append(row)
        print('row', row)


st.text('Clients')
st.table(data)
collection_watch = clients_ref.on_snapshot(on_snapshot)
