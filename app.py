import streamlit as st
from utils.firebase import init_firebase
from firebase_admin import firestore
import asyncio

# Initialize the Firebase Admin SDK
init_firebase()

# Get a reference to the Firestore database
clients_ref = firestore.client().collection('clients')

data = []


async def get_data():
    snapshot = await clients_ref.get()
    for doc in snapshot:
        client_data = doc.to_dict()
        row = [
            client_data['name'],
            # client_data['inviteEmails'],
        ]
        data.append(row)
        print('row', row)


async def display_table():
    while len(data) == 0:
        await asyncio.sleep(1)
    st.table(data)


async def main():
    tasks = [get_data(), display_table()]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    st.text('Clients')
    asyncio.run(main())
