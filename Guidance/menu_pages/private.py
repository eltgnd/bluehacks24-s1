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
        page_title = "Support Group Chat",
        page_icon = emoji,
        initial_sidebar_state = "expanded",
    )

    # Caption
    st.caption('BUGHAW   |   GUIDANCE COUNSELORS\' PORTAL')
    
    # Load initial data if it hasn't already been loaded.
    cf.load_initial_data_if_needed()

    st.title(f"{emoji} Support Group Chat")
    st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.')
    st.divider()

    user_id = st.session_state["counselor_id"]

    conn = groupchat_connect_to_user_database()

    @st.cache_data(max_entries = 10, ttl = 86400)
    def get_groupchat_info(user_id):
        result_df1 = conn.query(sql=f"SELECT * FROM Sheet1 WHERE user_id == '{user_id}';", ttl = 0).reset_index(drop = True)

        result_df2 = conn.query(sql=f"SELECT * FROM Sheet1 WHERE assigned_counselor == '{user_id}';", ttl = 0)
        
        info = {
            "groupchat_id_list": list(sorted(result_df1.at[0, "moderating_groupchats"].split(";"), reverse = False)),
            "assigned_student_id_list": list(result_df2["user_id"].sort_values(ascending = True).unique())
        }

        return info

    info = get_groupchat_info(user_id)
    
    chat_id_list = info["assigned_student_id_list"]
    keyword = "guidance"

    # Preparations to display messages

    if f"existing_messages_df_full" in st.session_state: # This is IN, not "NOT IN"
        existing_df_full = st.session_state[f"existing_messages_df_full"]

    if "clear_messages" not in st.session_state:
        st.session_state["clear_messages"] = False

    if "send_message_was_just_clicked" not in st.session_state:
        st.session_state["send_message_was_just_clicked"] = False

    if "support_open_chat" not in st.session_state:
        st.session_state["support_open_chat"] = False

    # Select group chat

    def open_chat_callback(decision):
        st.session_state["support_open_chat"] = decision

    # Select group chat
    selected_student_id = st.selectbox(
        "Select a student to chat with",
        options = chat_id_list,
        index = 0,
        args = (False,),
        on_change = open_chat_callback
    )

    selected_groupchat_id = f"PRIVATE_{selected_student_id}_{user_id}"

    open_chat_button = st.button("Open chat", args = (True,), on_click = open_chat_callback)

    if not st.session_state["support_open_chat"]:
        st.stop()

    # Container for displaying messages, above message input box
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

            new_row = pd.Series({"groupchat_id": selected_groupchat_id, "time": str(dt.datetime.now(dt.timezone(dt.timedelta(hours=8)))), "user_id": user_id, "message": new_message})

            new_row_df = pd.DataFrame([new_row], index = [0])

            new_df = pd.concat(
                objs = [existing_df_full, new_row_df],
                axis = 0,
                ignore_index = True
            )

        submitted_just_before_last_refresh = submitted
    
    # Display messages.
    # For demo only, query to get latest messages only runs when the page is opened and after you send a message, or every 2 minutes.

    if submitted_just_before_last_refresh:
        messages = new_df
    
    while True:

        if not submitted_just_before_last_refresh:
            with st.spinner("Refreshing messages..."):
                messages = conn.query(sql=f"SELECT * FROM Sheet2;", ttl = 3).dropna(axis = 0, how = "all")

        full_messages = messages.reset_index(drop = True)

        display_messages = full_messages.loc[full_messages["groupchat_id"] == selected_groupchat_id].sort_values("time", ascending = False).iloc[:20].sort_values("time", ascending = True)

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