import streamlit as st
import pandas as pd

# This is cached. The `max_entries` here is only 1 because the initial data and initial contents of session state are supposed to be the same for ALL users.
@st.cache_data(max_entries = 1)
def get_initial_data():
    """Read the files in the datasets folder of the app repository. Create a dictionary of (str: Any) pairs containing this and other initial information necessary across pages of the app. Return the dictionary."""

    # Color hex codes are defined here for consistency across charts.
    # To access these values in any page of the app, you can do this for example:
    # hexes = st.session_state["COLOR_HEXES"]
    # hexes["black"]

    color_hexes = {
        "black": "#000000",
        "white": "#ffffff",
        "light_gray": "#d3d3d3",
        "dark_gray": "#5b5b5b",
        "purple": "#4b0082",
        "magenta": "#e60087",
        "red": "#990000",
        "orange": "#c48520",
        "teal": "#4aa09f",
        "blue": "#3d85c6"
    }

    # Make a dictionary of items to put in the Streamlit session state.
    # For clarity, use the ff. conventions.
    # Constants (things that are meant not to change once they've been defined at the start of the session) are named in ALL CAPS.
    # Variables (things that change throughout the session) are named in all lowercase letters, or, they start with an uppercase substring and the rest of the letters are lowercase.
    initial_data = {
        "COLOR_HEXES": color_hexes,

        
    }

    return initial_data

# Do not cache
def load_initial_data_if_needed(force = False):
    """Load data if it hasn't already been loaded."""

    # When the app is initialized (meaning, the current user's session has just started), the initial_data_is_loaded key does NOT exist at all in session state.
    # Thus, the is_needed variable is True if the app has just been initialized and False otherwise.
    is_needed = "initial_data_is_loaded" not in st.session_state

    # If the app has just been initialized, or we specified `force` as True, the following will happen.
    if is_needed or force:
        initial_data = get_initial_data()
        update_session_state(initial_data, skip_if_key_exists = True)
        st.session_state["initial_data_is_loaded"] = True # Note this is just a placeholder value for the variable. What matters is whether the variable exists or not in session state.

    # No `else` block.

    return None

# Do not cache
def update_session_state(dct, skip_if_key_exists = False):
    """Take a dictionary `dct` and update the Streamlit session state using its key-value pairs.
    
The parameter `skip_if_key_exists` is False by default. For example, if dct = {"var1": 5}, then the value under "var1" in session state will be OVERWRITTEN by the numeric object 5.

If `skip_if_key_exists` is True, then it will check whether each key is already in session state. IF THE KEY IS ALREADY THERE, THEN ITS VALUE WILL NOT BE UPDATED."""
    for key, value in dct.items():
        if skip_if_key_exists:
            if key in st.session_state:
                continue # Skip to the next iteration without updating this key in session state.
        st.session_state[key] = value
    return

# Do not cache
def display_copyright():
    """Use Streamlit elements to display a copyright statement intended to be shown at the bottom of each page in the app."""

    st.markdown("---")
    st.caption("© 2023 (AUTHOR NAMES).")