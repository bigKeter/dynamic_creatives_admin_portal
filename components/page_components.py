import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder


def print_data(data):
    # Create pandas df
    df = pd.DataFrame(data)

    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination()  # Add pagination
    gb.configure_side_bar()  # Add a sidebar
    gb.configure_selection(
        "multiple",
        use_checkbox=True,
        groupSelectsChildren="Group checkbox select children",
    )  # Enable multi-row selection
    gridOptions = gb.build()

    grid_response = AgGrid(
        df,
        gridOptions=gridOptions,
        data_return_mode="AS_INPUT",
        update_mode="MODEL_CHANGED",
        fit_columns_on_grid_load=True,
        theme="streamlit",  # Add theme color to the table
        enable_enterprise_modules=True,
        height=350,
        width="100%",
        reload_data=False,
        enable_quicksearch=True,
    )

    data = grid_response["data"]
    selected = grid_response["selected_rows"]
    df = pd.DataFrame(selected)
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
    return grid_response


def selectbox(label, options):
    return st.selectbox(label=label, options=options)
