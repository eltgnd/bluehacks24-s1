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

        st.write(df)

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