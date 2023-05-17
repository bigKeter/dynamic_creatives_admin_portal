# 0_Clients.py
import asyncio
from datetime import datetime

import streamlit as st

from components.page_components import print_data, selectbox
from utils.utils import create_doc, get_docs, get_names, get_reference, process_doc_refs

# Create a new event loop and set it as the current event loop, this will hold the event queue of the async functions we'll call, usually only one event loop is needed
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# Get clients and users data from database
clients_docs = loop.run_until_complete(get_docs("clients"))
users_docs = loop.run_until_complete(get_docs("users"))

# Set page config and info
st.set_page_config(page_title="Clients Page", page_icon="👥")
st.sidebar.header("Clients Page")
st.subheader(
    """
    This page contains data about clients.
    """
)

# Call async function to run event loop
clients = loop.run_until_complete(process_doc_refs(clients_docs))
user_names = loop.run_until_complete(get_names(users_docs))

# Print the data
print_data(clients)

# Expander to add new client
with st.sidebar:
    with st.expander("Add new client"):
        name = st.text_input("name")
        inviteEmail = st.text_input("inviteEmail")
        users = selectbox("Existing Users", user_names)
        submit = st.button("Add new client")

        if submit:
            users_ref = loop.run_until_complete(get_reference("users", users))

            object = {
                "name": name,
                "inviteEmail": inviteEmail,
                "users": users_ref,
                "createdAt": datetime.now(),
            }
            loop.run_until_complete(create_doc(object, "clients"))
