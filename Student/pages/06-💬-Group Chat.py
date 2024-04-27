import streamlit as st
import pandas as pd
import numpy as np
from streamlit_gsheets import GSheetsConnection
import time

import control_flow as cf

@st.cache_resource(ttl=86400, max_entries = 1)
def connect_to_user_database(user_id):
    conn = st.connection("user", type=GSheetsConnection)

    result_df = conn.read(worksheet = "Sheet1", ttl = None) # Not sure about ttl
    # first_row = result_df.loc[result_df["user_id"] == user_id].iloc[0]

    st.write(result_df["user_id"] == user_id)
    
    info = {
        "assigned_counselor": first_row["assigned_counselor"],
        "groupchat_id": first_row["groupchat_id"]
    }

    return conn, info

if __name__ == "__main__":

    emoji = ":speech_balloon:"

    st.set_page_config(
        page_title = "Group Chat",
        page_icon = emoji,
        initial_sidebar_state = "expanded",
    )

    # Load initial data if it hasn't already been loaded.
    cf.load_initial_data_if_needed()

    st.markdown("(PROJECT TITLE)") # Name of our project will be displayed in small text above the current page title.
    st.title(f"{emoji} Group Chat")

    conn, info = connect_to_user_database(user_id = st.session_state["student_id"])

    selected_chat = st.radio(
        "Chat",
        ["Support Group", "Your Counselor"],
        horizontal = True
    )

    if selected_chat == "Support Group":
        st.markdown("### Support Group")

        st.write(info['groupchat_id'])

        while True:
            query = f"""SELECT *
FROM Sheet2
WHERE groupchat_id == {info['groupchat_id']}
ORDER BY time DESC
LIMIT 100
;
"""
            messages = conn.query(sql=query)  # default ttl=3600 seconds / 60 min
            st.dataframe(messages.sort_values("time", ascending = True))
            time.sleep(1)

    else: # Your Counselor
        st.markdown("### Your Counselor")