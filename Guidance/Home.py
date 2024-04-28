import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_gsheets import GSheetsConnection
from st_pages import Page, Section,show_pages, add_page_title
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_image_select import image_select
import control_flow as cf
import datetime
from PIL import Image

# Page config
st.set_page_config(page_title='Bughaw Counselors\' Portal', page_icon='💙', layout="centered", initial_sidebar_state="auto", menu_items=None)

# Google Sheets Connection
conn = st.connection("user", type=GSheetsConnection)

# Initialize
cf.load_initial_data_if_needed(force = True)
placeholder = st.empty()

# Title
st.image('images/BUGHAW.png', width=100)
add_vertical_space(1)
st.caption('BUGHAW   |   GUIDANCE COUNSELORS\' PORTAL')

add_vertical_space(1)
login_placeholder = st.empty()
with login_placeholder:
    st.markdown(f"""
        <div style="line-height:450%;">
            <span style=" font-size:80px ; color:#023E8A ; font-weight:bold; ">From blue </span>
            <span style=" font-size:80px ; color:#31333F ; font-weight:bold; ">to hue</span>
            <span style=" font-size:80px ; color:#31333F ; font-weight:bold; ">.</span>
        </div>""",
        unsafe_allow_html=True
    )

placeholder = st.empty()
with placeholder:
    with st.container(border=True):
        st.write('🔓 Try this sample counselor ID: g001, password: hello456')

# User Authentication
def check_password():
    # Log-in
    def log_in():
        with st.form('Credentials'):
            st.text_input("Enter your counselor ID", type='default', key='counselor_id_input')
            st.text_input("Enter your password", type="password", key="password")
            st.form_submit_button("Log-in", on_click=password_entered)
 
    def password_entered():
        sql = 'SELECT * FROM Sheet1;'
        df = conn.query(sql=sql, ttl=0) 
        match = (df['user_id'].eq(st.session_state.counselor_id_input) & df['password'].eq(st.session_state.password)).any()
        if match:
            st.session_state["password_correct"] = True  
            st.session_state['counselor_id'] = st.session_state.counselor_id_input
            st.session_state['name'] = df[df.user_id == st.session_state.counselor_id].reset_index().at[0,'nickname']
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

# Start
login_placeholder.empty()
placeholder.empty()

st.markdown(f"""
    <div style="line-height:450%;">
        <span style=" font-size:60px ; color:#31333F ; font-weight:bold; ">Welcome, </span>
        <span style=" font-size:60px ; color:#023E8A ; font-weight:bold; ">{st.session_state.name}</span>
        <span style=" font-size:60px ; color:#31333F ; font-weight:bold; ">👋</span>
    </div>""",
    unsafe_allow_html=True
)

# Welcome
show_pages(
    [
        Page('Home.py', 'Homepage', '👤'),
        Page('menu_pages/appointments.py', 'Manage Appointments', '📋'),
        Page('menu_pages/private.py', 'Private Chat', '💬'),
        Page('menu_pages/support.py', 'Support Group Chat', '🫂'),
        Page('menu_pages/survey.py', 'Data Analytics', '📊'),
        Page('menu_pages/about.py', 'About', '💡'),
    ]
)

# Information about the app
st.write('Welcome to Bughaw Counselors\' Portal. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.')
col1, col2 = st.columns(2)
with col1:
    with st.expander(label='WHAT IS BUGHAW', expanded=False):
        st.write('Lorem ipsum')
with col2:
    with st.expander(label='WHY BUGHAW'):
        section_text = ''
        st.markdown(f"**:blue[Ratio something something.]**\n\n{section_text}")

# About Bughaw
st.header('Get to know your Bughaw!')

# Impact
st.caption('IMPACT BY NUMBERS')
col1, col2, col3 = st.columns(3)
row1= [col1, col2, col3]
homepage_impact = {
    0 : ['Active Students', '2748 🧑‍🎓', 1406],
    1 : ['Successful Consultations', '376 🫂', 8],
    2 : ['Mental Health Volunteers', '49 💙', 16]

}
for ind, col in enumerate(row1):
    col.metric(label=homepage_impact[ind][0], value=homepage_impact[ind][1], delta=homepage_impact[ind][2])

style_metric_cards(border_left_color='#023E8A', border_radius_px=7, box_shadow=False)

st.divider()

# Features Overview
option = st.radio('Get to know Bughaw\'s features!', ['Appointment Calendar', 'Student Dashboard', 'Database Page', 'Group Chat System', 'Profile Tab'])
descriptions = {
'Appointment Calendar':"",
'Student Dashboard':"",
'Database Page':"",
'Group Chat System':"",
'Profile Tab':"The Profile Tab is a repository of your personal information that also allows you to track your own mental health journey through a series of easily comprehensible statistical analysis of your past survey responses."
}

with st.container(border=True):
    st.subheader(option)
    st.write(descriptions[option])