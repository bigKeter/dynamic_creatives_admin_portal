# app.py
import asyncio
import streamlit as st
import json
from typing import Coroutine, Any
from firebase_admin import firestore
from utils.firebase_init import init_firebase

init_firebase()
db = firestore.client()


async def get_docs() -> Coroutine[Any, Any, None]:
    # Get documents from database
    docs = db.collection('clients').stream()

    # Yield documents one at a time
    async def generate_docs():
        for doc in docs:
            yield doc
        yield None

    # Return an asynchronous iterable
    return generate_docs()

# define async function to get a referenced document from the database


async def get_doc(doc_ref):
    # Get document from database
    doc = doc_ref.stream()

    # Return document
    return doc


async def process_docs(docs):
    # Do something with documents
    res = []
    async for doc in docs:
        if doc is None:
            break
        print(doc.to_dict())
        res.append(doc.to_dict())

    return res

# Define async function to run event loop


async def main():

    # Get clients from the database
    clients = await process_docs(await get_docs())

    # Convert Arrow objects to strings
    for client in clients:
        client['users'] = str(client['users'])
        client['briefs'] = str(client['briefs'])

    # Display a table with each client name and a list of invited users as tags
    st._arrow_dataframe(clients)

# Create a new event loop and set it as the current event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# Call async function to run event loop
loop.run_until_complete(main())
