import pandas as pd
import streamlit as st


def print_data(data):
    # Create pandas df
    df = pd.DataFrame(data)

    # if "pressed" not in st.session_state:
    #     st.session_state.pressed = False

    # def change_state():
    #     st.session_state.pressed = not st.session_state.pressed

    # Toggle button
    # st.button("Edit Data", help="Activate edit mode.")

    # Display the data based on the toggle state
    # if st.session_state.pressed:
    #     return st.experimental_data_editor(df, num_rows="dynamic")
    # else:
    return st.dataframe(df)


def selectbox(label, options):
    return st.selectbox(label=label, options=options)
