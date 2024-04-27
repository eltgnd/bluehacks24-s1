import streamlit as st
from PIL import Image
global name
global mood

global experience

# parameters for now, this will come from survey page:
mood = 'Happy'
name = 'Osen'
experience = 999

st.title("🧑 Profile")
st.write(f'Hello {name}!')
st.write(f'Current Mode: {mood}')
st.write(f'Current Level: {experience//100}!')

#@Val write statistics here:
profile_sidebar()

# Title
st.title(f'Welcome {st.session_state.name}!')
st.write(f'Student ID: {st.session_state.student_id}')

# General Survey
st.header('General Wellbeing')
sql = f'SELECT "General " FROM Sheet1 WHERE "Student ID" = {st.session_state.student_id} ORDER BY Date;'
df = conn.query(sql=sql)







