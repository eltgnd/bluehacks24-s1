import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_gsheets import GSheetsConnection
from st_pages import Page, Section,show_pages, add_page_title
from streamlit_extras.switch_page_button import switch_page
import control_flow as cf
from PIL import Image

global name
global mood
global experience

# parameters for now, this will come from survey page:
mood = 'Happy'
name = 'Osen'
experience = 999

# Initialize
st.set_page_config(page_title='[NAME] Students\' Portal', page_icon='🌱', layout="centered", initial_sidebar_state="auto", menu_items=None)
cf.load_initial_data_if_needed(force = True)

# Google Sheets Connection
conn = st.connection("user", type=GSheetsConnection)

# Title
st.caption('Student Page')
st.title('Welcome')
add_vertical_space(2)


# User Authentication
def check_password():

    # Sample
    st.write('Try this sample student ID: 222390, password: 123456')

    # Log-in
    def log_in():
        with st.form('Credentials'):
            st.text_input("Enter your student ID", type='default', key='student_id')
            st.text_input("Enter your password", type="password", key="password")
            st.form_submit_button("Log-in", on_click=password_entered)
 
    def password_entered():
        sql = 'SELECT * FROM Sheet1;'
        df = conn.query(sql=sql, ttl=0) 
        match = (df['user_id'].eq(st.session_state.student_id) & df['password'].eq(st.session_state.password)).any()
        if match:
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

# Profile at bottom left of sidebar
def profile_sidebar():
    def image_to_base64(image):
        import base64
        import io
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()

    background_image = Image.open("images/background.png")
    if mood == 'Happy':
        cat_image = Image.open("images/cat_happy.png")
    elif mood == 'Amused':
        cat_image = Image.open("images/cat_amused.png")
    elif mood == 'Inspired':
        cat_image = Image.open("images/ccat_inspired.png")
    elif mood == 'Dont Care':
        cat_image = Image.open("images/ccat_dont_care.png")
    elif mood == 'Annoyed':
        cat_image = Image.open("images/ccat_annoyed.png")
    elif mood == 'Afraid':
        cat_image = Image.open("images/ccat_afraid.png")
    elif mood == 'Sad':
        cat_image = Image.open("images/ccat_sad.png")
    elif mood == 'Angry':
        cat_image = Image.open("images/ccat_angry.png")


    # Calculate level and remaining experience
    level = experience // 100
    remaining_experience = experience % 100

    # Calculate width of level bar based on remaining experience
    level_bar_width = remaining_experience / 100 * 150  # Percentage of 100 pixels

    # Display stacked images with text
    with st.sidebar:
        st.write(
        f"""
        <div style="position:relative;">
            <img src="data:image/png;base64,{image_to_base64(background_image)}" style="width:100%;">
            <img src="data:image/png;base64,{image_to_base64(cat_image)}" style="position:absolute;top:50%;left:50%;transform:translate(-50%, -50%);width:75%">
        </div>
        """,
        unsafe_allow_html=True
    )
