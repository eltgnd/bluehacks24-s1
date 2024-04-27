"""
File description
"""

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Custom functions
import control_flow as cf

if __name__ == "__main__":

    emoji = ":mag:"

    page_title = "PAGE TITLE"

    st.set_page_config(
        page_title = page_title,
        page_icon = emoji,
        initial_sidebar_state = "expanded",
    )

    # Show logo and title
    logo_and_title_cols = st.columns([1, 6])

    with logo_and_title_cols[0]:
        # Load logo image
        logo = Image.open("images/logo.png")
        st.image(
            image = logo,
            width = 90,
            output_format = "JPEG"
        )
    with logo_and_title_cols[1]:
        st.title(page_title)

    # Force-load initial data.
    # We should use force = False in other pages.
    cf.load_initial_data_if_needed(force = True)

    st.markdown("""Welcome!

(App description)

""")
    
    cf.display_copyright()