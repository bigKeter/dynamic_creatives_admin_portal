# 2_Talents.py
from utils.utils import process_docs, get_docs
from components.page_components import edit_button as grid
import streamlit as st
import asyncio

async def spawn_talents():
    talents = await process_docs(await get_docs("talents"))
    grid(talents)

st.set_page_config(page_title="Talents Page", page_icon="⭐")
st.sidebar.header("Talents Page")
st.write(
    """
    This page contains data about talents.
    """)

# Create a new event loop and set it as the current event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# Call async function to run event loop
loop.run_until_complete(spawn_talents())