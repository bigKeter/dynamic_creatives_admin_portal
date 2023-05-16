# 1_Briefs.py
from utils.utils import process_docs, get_docs
from components.page_components import edit_button as grid
import streamlit as st
import asyncio

async def spawn_briefs():
    briefs = await process_docs(await get_docs("briefs"))
    grid(briefs)

st.set_page_config(page_title="Briefs Page", page_icon="📝")
st.sidebar.header("Briefs Page")
st.write(
    """
    This page contains data about briefs.
    """)

# Create a new event loop and set it as the current event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# Call async function to run event loop
loop.run_until_complete(spawn_briefs())