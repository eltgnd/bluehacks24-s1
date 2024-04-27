import streamlit as st

import control_flow as cf

if __name__ == "__main__":

    emoji = ":page_facing_up:"

    st.set_page_config(
        page_title = "(PAGE TITLE)",
        page_icon = emoji,
        initial_sidebar_state = "expanded",
    )

    # Load initial data if it hasn't already been loaded.
    cf.load_initial_data_if_needed()

    st.markdown("(PROJECT TITLE)") # Name of our project will be displayed in small text above the current page title.
    st.title(f"{emoji} (PAGE TITLE)")

    # ---------
    # Put page content here.

    

    # ---------
    
    cf.display_copyright()