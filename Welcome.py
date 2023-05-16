# app.py
import streamlit as st

# Set welcome page info
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to your data! 👋")

st.sidebar.header("Welcome")
st.sidebar.success("Select a page from above.")
