import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_gsheets import GSheetsConnection
from st_pages import Page, Section,show_pages, add_page_title
from streamlit_extras.switch_page_button import switch_page
import control_flow as cf

# Initialize
st.set_page_config(page_title='[NAME] Students\' Portal', page_icon='🌱', layout="centered", initial_sidebar_state="auto", menu_items=None)
cf.load_initial_data_if_needed(force = True)

# Google Sheets Connection
member_database = st.secrets['student_database']
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet=member_database)


# Title
st.caption('Student Page')
add_vertical_space(1)
st.title('Welcome')
add_vertical_space(2)


# User Authentication
def check_password():

    # Sample
    st.write('Try this sample student ID: 222390')

    # Log-in
    def log_in():
        with st.form('Credentials'):
            st.text_input("Enter your User ID")
            st.text_input("Enter your password", type="password", key="password")
            st.form_submit_button("Log-in", on_click=password_entered)
 
    def password_entered():
        if df['Student ID'].eq(st.session_state['password']).any():
            st.session_state["password_correct"] = True

            # store member info from database
            member_id = st.session_state['password']
            member_info = df[df['Student ID'] == member_id].to_dict('records')
            st.session_state['member_info'] = member_info
            
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct", False):
        return True

    log_in()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False

if not check_password():
    st.stop()


# Welcome
# show_pages(
#     [
#         Page('Admin/Home.py', 'Log-in', '👤'),
#         Page('Admin/menu_pages/dashboard.py', 'Project Blue Dashboard', '📊'),
#         Page('Admin/menu_pages/reports.py', 'Project Reports', '📄'),
#         Page('Admin/menu_pages/members.py', 'Members', '✋'),
#         Page('Admin/menu_pages/exit.py', 'Exit Process', '👋')
#     ]
# 
# )

# switch_page('project blue dashboard')
# hide_pages(['log-in'])
