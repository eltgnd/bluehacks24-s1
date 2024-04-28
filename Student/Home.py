import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_gsheets import GSheetsConnection
from st_pages import Page, Section,show_pages, add_page_title, hide_pages
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_image_select import image_select
import control_flow as cf
from streamlit.components.v1 import html
import datetime
from PIL import Image

st.set_page_config(page_title='Bughaw Students\' Portal', page_icon='💙', layout="centered", initial_sidebar_state="auto", menu_items=None)

hide_pages(['meditate', 'read', 'study'])

# Google Sheets Connection
conn = st.connection("user", type=GSheetsConnection)

# Update Google sheets
def update_data(survey_type):
    df = conn.read(worksheet='Sheet1', ttl=0)
    now = datetime.datetime.now()

    df.loc[len(df.index)] = [
        st.session_state.student_id,
        now,
        st.session_state.ga if survey_type=='g' else None,
        st.session_state.ma if survey_type=='m' else None,
        st.session_state.mood if survey_type=='d' else None
    ]

    conn.update(worksheet="Sheet1", data=df)
    st.success("Worksheet Updated! 🥳")


# Initialize
cf.load_initial_data_if_needed(force = True)

# Title
# st.image(logo_imglink, width=100)
add_vertical_space(1)
st.caption('BUGHAW   |   STUDENTS\' PORTAL')

add_vertical_space(1)
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
        st.write('🔓 Try this sample student ID: s222869, password: hello876')

# User Authentication
def check_password():
    # Log-in
    def log_in():
        with st.form('Credentials'):
            st.text_input("Enter your student ID", type='default', key='student_id_input')
            st.text_input("Enter your password", type="password", key="password")
            st.form_submit_button("Log-in", on_click=password_entered)
 
    def password_entered():
        sql = 'SELECT * FROM Sheet1;'
        df = conn.query(sql=sql, ttl=0) 
        match = (df['user_id'].eq(st.session_state.student_id_input) & df['password'].eq(st.session_state.password)).any()
        if match:
            st.session_state["student_id"] = st.session_state.student_id_input
            st.session_state["password_correct"] = True  
            st.session_state['name'] = df[df.user_id == st.session_state.student_id].reset_index().at[0,'nickname']
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
placeholder.empty()

# Information about the app
st.write('Welcome to Bughaw Students\' Portal. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.')
col1, col2 = st.columns(2)
with col1:
    with st.expander(label='WHAT IS BUGHAW', expanded=False):
        st.write('Lorem ipsum')
with col2:
    with st.expander(label='WHY BUGHAW'):
        section_text = ''
        st.markdown(f"**:blue[Ratio something something.]**\n\n{section_text}")

# Daily wellbeing
st.session_state.mood_button = False
with st.expander(label=f'📅 How are you today, {st.session_state.name}?'):
    st.write(f"🌱 Selet your mood for today by clicking on the corresponding image.")
    mood_lst = ["Happy", "Amused", "Inspired", "Don't Care", "Annoyed", "Afraid", "Sad", "Angry"]

    # Display mood images and get user input
    selected_mood = image_select(label="", images=["images/8_happy.png", "images/7_amused.png", 
                                                "images/6_inspired.png", "images/5_dont_care.png",
                                                "images/4_annoyed.png", "images/3_afraid.png",
                                                "images/2_sad.png", "images/1_angry.png"], 
                                                use_container_width=False,
                                                captions=["Happy", "Amused", "Inspired", "Don't Care",
                                                            "Annoyed", "Afraid", "Sad", "Angry"],
                                                    return_value="index")
    st.session_state.mood = mood_lst[int(str(selected_mood)[:100])]

    button = st.button('Submit')

    if button:
        st.session_state.mood_button = True
    
    if st.session_state.mood_button:
        update_data('d')

# Welcome
show_pages(
    [
        Page('Home.py', 'Homepage', '👤'),
        Page('menu_pages/wellbeing.py', 'Student Wellbeing', '📊'),
        Page('menu_pages/profile.py', f'{st.session_state.name}\'s Profile', '🧑'),
        Page('menu_pages/toolkit.py', f'{st.session_state.name}\'s Toolkit', '🛠️'),
        Page('menu_pages/appointment.py', 'Set an Appointment', '📄'),
        Page('menu_pages/support.py', 'Chat with Support Group', '🫂'),
        Page('menu_pages/counselor.py', 'Chat with Counselor', '💬'),
        Page('menu_pages/about.py', 'About', '💡'),
        
    ]

)

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
option = st.radio('Get to know Bughaw\'s features!', ['Mental Health Feed', 'Student Wellbeing', 'Book Appointment', 'Profile', 'Group Chat'])
descriptions = {
'Mental Health Feed':'The Mental Health Feed displays collated articles from various websites that specifically address and provide tips about mental health, such as but not limited to HelpGuide.org and Science Daily',
'Student Wellbeing':'The Student Dashboard serves as a regular mental wellbeing check-in surveys for your daily mood, weekly general health status, and monthly sense of coherence that altogether holistically assess the status of your mental health.',
'Book Appointment':'The Appointment Scheduler is an efficient, go-to, guided scheduler that allows you to book an appointment with a guidance counselor. This includes a quick look at the counselor’s monthly calendar to proactively determine free slots, as well as a request form that caters to your anonymity.',
'Group Chat': '',
'Profile':'The Profile Tab is a repository of your personal information that also allows you to track your own mental health journey through a series of easily comprehensible statistical analysis of your past survey responses.',
'Group Chat':'The About Tab is a quick briefer and information tab about Bughaw, its purpose, limitations, as well as the references used all  throughout the website.'
}

with st.container(border=True):
    st.subheader(option)
    st.write(descriptions[option])