import streamlit as st
from utils.firebase import init_firebase
from firebase_admin import firestore
import asyncio
import builtins

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


@st.cache(hash_funcs={builtins.coroutine: id})
async def run_async():
    await get_data()
    await display_table()


def main():
    st.text('Clients')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_async())


if __name__ == '__main__':
    main()
