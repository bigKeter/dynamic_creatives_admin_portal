import asyncio
from typing import Any, Coroutine

import streamlit as st
from firebase_admin import firestore

from utils.firebase_init import init_firebase

init_firebase()
db = firestore.client()


async def async_get(doc_ref):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, doc_ref.get)


async def get_docs(collection_name) -> Coroutine[Any, Any, None]:
    # Get documents from database
    docs = db.collection(collection_name).stream()

    # Yield documents one at a time
    async def generate_docs():
        for doc in docs:
            yield doc
        yield None

    # Return an asynchronous iterable
    return generate_docs()


async def process_doc_refs(docs):
    # Do something with documents
    res = []
    async for doc in docs:
        if doc is None:
            break
        data = doc.to_dict()
        keys = data.keys()

        for key in keys:
            match key:
                case "users":
                    user_refs = data[
                        "users"
                    ]  # Get the user ref from the 'users' field, in the form of a DocumentReference from the main doc
                    if not isinstance(user_refs, list):
                        user_refs = [
                            user_refs
                        ]  # Convert to a list if it's a single DocumentReference, so that the iteration below works
                    user_docs = await asyncio.gather(
                        *(
                            async_get(user_ref) for user_ref in user_refs
                        )  # Use the ref in the key to get the actual doc from the users collection, which itself has a 'name' field
                    )
                    data["users"] = [
                        user_doc.to_dict()["name"]
                        for user_doc in user_docs  # Get the content of the 'name' field from the user doc in the users collection and replace the user ref from the original doc with it (temporarily, since data is a local variable)
                    ]
                case "briefs":
                    brief_refs = data["briefs"]
                    if not isinstance(brief_refs, list):
                        brief_refs = [brief_refs]
                    brief_docs = await asyncio.gather(
                        *(async_get(brief_ref) for brief_ref in brief_refs)
                    )
                    data["briefs"] = [
                        brief_doc.to_dict()["name"] for brief_doc in brief_docs
                    ]
                case "talent":
                    talent_refs = data["talent"]
                    if not isinstance(talent_refs, list):
                        talent_refs = [
                            talent_refs
                        ]  # Convert to a list if it's a single DocumentReference
                    talent_docs = await asyncio.gather(
                        *(async_get(talent_ref) for talent_ref in talent_refs)
                    )
                    data["talents"] = [
                        talent_doc.to_dict()["name"] for talent_doc in talent_docs
                    ]
                case "client":
                    client_refs = data["client"]
                    if not isinstance(client_refs, list):
                        client_refs = [
                            client_refs
                        ]  # Convert to a list if it's a single DocumentReference
                    client_docs = await asyncio.gather(
                        *(async_get(client_ref) for client_ref in client_refs)
                    )
                    data["clients"] = [
                        client_doc.to_dict()["name"] for client_doc in client_docs
                    ]

        res.append(data)

    return res


async def get_names(docs):
    # Do something with documents
    names = []
    async for doc in docs:
        if doc is None:
            break
        data = doc.to_dict()
        names.append(data["name"])
    return names


async def create_doc(data, collection_name):
    # Create a new document in the database
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(
        None, lambda: db.collection(collection_name).document().set(data, merge=True)
    )
    st.success("Document created successfully!")


async def get_reference(collection_name, doc_name):
    query = db.collection(collection_name).where("name", "==", doc_name)
    docs = query.stream()
    for doc in docs:
        if doc is None:
            break
        return doc.reference
