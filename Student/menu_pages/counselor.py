import streamlit as st
import pandas as pd
import numpy as np
from streamlit_gsheets import GSheetsConnection
import time
import datetime as dt

import control_flow as cf

@st.cache_resource(ttl=86400, max_entries = 1)
def groupchat_connect_to_user_database():
    conn = st.connection("user", type=GSheetsConnection)

    return conn

if __name__ == "__main__":

    emoji = ":speech_balloon:"

    st.set_page_config(
        page_title = "Counselor Chat",
        page_icon = emoji,
        initial_sidebar_state = "expanded",
    )

    # Load initial data if it hasn't already been loaded.
    cf.load_initial_data_if_needed()

    st.caption('BUGHAW   |   STUDENTS\' PORTAL')
    st.title(f"{emoji} Counselor Chat")
    st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.')
    st.divider()

    conn = groupchat_connect_to_user_database()

    @st.cache_data(max_entries = 10, ttl = 86400)
    def get_groupchat_info(user_id):
        result_df = conn.query(sql=f"SELECT * FROM Sheet1 WHERE user_id == '{user_id}'", ttl = 0)
        first_row = result_df.iloc[0]
        
        info = {
            "assigned_counselor": first_row["assigned_counselor"],
            "groupchat_id": first_row["groupchat_id"]
        }

        return info
    
    user_id = st.session_state["student_id"]

    info = get_groupchat_info(user_id)
    
    assigned_counselor = info["assigned_counselor"]
    groupchat_id = info["groupchat_id"]

    st.markdown("### Counselor Chat")
    # Instead of using the student's groupchat, use the private chat between the student and the counselor.
    groupchat_id = f"PRIVATE_{user_id}_{assigned_counselor}"
    keyword = "counselor"

    # Preparations to display messages

    if f"existing_messages_df_full" in st.session_state: # This is IN, not "NOT IN"
        existing_df_full = st.session_state[f"existing_messages_df_full"]

    if "clear_messages" not in st.session_state:
        st.session_state["clear_messages"] = False

    if "send_message_was_just_clicked" not in st.session_state:
        st.session_state["send_message_was_just_clicked"] = False

    chat_empty = st.empty()

    # Input message

    with st.form("input message", clear_on_submit = True):
        form_cols = st.columns([9,1])
        with form_cols[0]:
            new_message = st.text_area("Send a message", max_chars = 500, label_visibility = "hidden")
            # Every form must have a submit button.
        with form_cols[1]:
            submitted = st.form_submit_button(
                ":leftwards_arrow_with_hook:",
            )

        if submitted:

            new_row = pd.Series({"groupchat_id": groupchat_id, "time": str(dt.datetime.now(dt.timezone(dt.timedelta(hours=8)))), "user_id": user_id, "message": new_message})

            new_row_df = pd.DataFrame([new_row], index = [0])

            new_df = pd.concat(
                objs = [existing_df_full, new_row_df],
                axis = 0,
                ignore_index = True
            ).sort_values("time", ascending = True)

        submitted_just_before_last_refresh = submitted
    
    # Display messages.
    # For demo only, query to get latest messages only runs when the page is opened and after you send a message, or every 2 minutes.

    if submitted_just_before_last_refresh:
        messages = new_df
    
    while True:

        if not submitted_just_before_last_refresh:
            messages = conn.query(sql=f"SELECT * FROM Sheet2;", ttl = 3).dropna(axis = 0, how = "all")

            # # removed:
            #  WHERE groupchat_id == '{groupchat_id}' ORDER BY time DESC

        full_messages = messages.reset_index(drop = True)

        display_messages = full_messages.loc[full_messages["groupchat_id"] == groupchat_id].sort_values("time", ascending = False).iloc[:20].sort_values("time", ascending = True)

        st.session_state["existing_messages_df_full"] = full_messages

        chat_empty.empty()

        with chat_empty:
            with st.container():

                if display_messages.shape[0] == 0:
                    st.info("There are no messages in this chat yet.")
        
                else:
                    # Display messages
                    for index, row in display_messages.iterrows():
                        msg_time = row["time"].split(" ")[1][:8]
                        if row["user_id"] == user_id:
                            my_cols = st.columns([0.2,0.6,0.2])
                            with my_cols[1]:
                                # with st.container(border = True):
                                st.html(f'<p style = "text-align: right;">{row["message"]}</p>')
                            with my_cols[2]:
                                st.caption(msg_time)
                        else:
                            other_cols = st.columns([0.6,0.2,0.2])
                            with other_cols[0]:
                                # with st.container(border = True):
                                st.html(f'<p style = "text-align: left;"><b style = "color: gray;">[{row["user_id"]}] </b>{row["message"]}</p>')
                            with other_cols[2]:
                                st.caption(msg_time)

        if submitted_just_before_last_refresh:
            conn.update(worksheet = "Sheet2", data = full_messages)

        submitted_just_before_last_refresh = False 

        time.sleep(4)