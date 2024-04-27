import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from streamlit_extras.add_vertical_space import add_vertical_space
import datetime

# On-call function
def update_gq(ans):
    st.session_state.ga.append(ans)
    st.session_state.gq += 1

# Google Sheets Connection
conn = st.connection("survey", type=GSheetsConnection)

# Update Google sheets
def update_data(survey_type):
    df = conn.read(worksheet='Sheet1', ttl=0)
    now = datetime.datetime.now()

    df.loc[len(df.index)] = [
        st.session_state.student_id,
        now,
        st.session_state.ga if survey_type=='g' else None,
        st.session_state.ma if survey_type=='m' else None
    ]

    conn.update(worksheet="Sheet1", data=df)
    st.success("Worksheet Updated! 🥳")

def check_streak():
    sql = f'SELECT Date FROM Sheet1 WHERE "Student ID" = {st.session_state.student_id} ORDER BY Date;'
    df = conn.query(sql=sql)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date_Diff'] = df['Date'].diff().dt.days
    df['Streak_ID'] = (df['Date_Diff'] > 1).cumsum()
    streaks = df.groupby('Streak_ID').cumcount() + 1

    return streaks.max()
    


# Title
name = st.session_state.name
st.title(f'Hi {name.capitalize()}, kumusta ka? 👋')
st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.')

# Show streak
col1, col2, col3 = st.columns(3)
with col1:
    with st.container(border=True):
        st.metric('Answer Streak', f'{check_streak()} days', delta='Nice work!')

# Choose survey
with st.container(border=True):
    options = ['Weekly Well-being', 'Monthly Check-up']
    choice = st.radio('What do you want to answer?', options)

# General Health Questionnaire
if choice == options[0]:

    if 'gq' not in st.session_state:
        st.session_state.gq = 0
    if 'ga' not in st.session_state:
        st.session_state.ga = []
    if 'submitted_g' not in st.session_state:
        st.session_state_g = False

    questions = """I can concentrate regularly.
    I lose sleep over worrying.
    I play a useful role in the community.
    I can make the right decisions for myself.
    I am always under stress.
    I cannot overcome challenges.
    I enjoy day-to-day activities.
    I can face problems.
    I feel sad and anxious.
    I lose confidence.
    I see myself as worthless.
    I feel reasonably happy."""

    question_lst = questions.split('\n')

    add_vertical_space(1)
    st.write('💡 In a scale of 1 to 4, how well do you resonate with the following statements or questions?')

    # Place question
    options = [str(i) for i in range(1,5)]
    options[0] += ' (Least)'
    options[-1] += ' (Most)'

    if st.session_state.gq > 11:
        st.write('Successfully submitted!')
        update_data('g')
        st.session_state.submitted_g = True
    else:
        with st.container(border=True):
            st.caption(f'Question {st.session_state.gq + 1} of 12')
            ans = st.radio(question_lst[st.session_state.gq].strip(), options, horizontal=True, key=f'g{st.session_state.gq}')
            submit = st.button('Submit')

        if submit:
            st.session_state.gq += 1
            st.session_state.ga.append(ans)

# Monthly Check-up
if choice == options[1]:

    if 'mq' not in st.session_state:
        st.session_state.mq = 0
    if 'ma' not in st.session_state:
        st.session_state.ma = []
    if 'submitted_m' not in st.session_state:
        st.session_state_m = False

    questions = """Do you have the feeling that you don’t really care about what goes on around you?
    Has it happened in the past that you were surprised by the behaviour of people whom you thought you knew well?
    Has it happened that people whom you counted on disappointed you?
    Until now your life has had: no clear goals or purpose at all—very clear goals and purpose
    Do you have the feeling that you’re being treated unfairly?
    Do you have the feeling that you are in an unfamiliar situation and don’t know what to do?
    Doing the things you do every day is: a source of deep pleasure and satisfaction—a source of pain and boredom
    Do you have very mixed-up feelings and ideas?
    Does it happen that you have feelings inside you would rather not feel?
    Many people—even those with strong character—sometimes feel like sad losers in certain situations. How often have you felt this way in the past?
    When something has happened have you generally found that: you overestimated or underestimated its importance—you saw things in the right proportion
    How often do you have the feeling that there's little meaning in the things you doin your daily life?
    How often do you have the feeling that you’re not sure you can keep under control?"""

    question_lst = questions.split('\n')

    add_vertical_space(1)
    st.write('💡 In a scale of 1 to 7, how well do you resonate with the following statements or questions?')

    # Place question
    options = [str(i) for i in range(1,8)]
    options[0] += ' (Least)'
    options[-1] += ' (Most)'

    if st.session_state.gq > 12:
        st.write('Successfully submitted!')
        update_data('m')
        st.session_state.submitted_m = True

    else:
        with st.container(border=True):
            st.caption(f'Question {st.session_state.mq} of 13')
            ans = st.radio(question_lst[st.session_state.mq].strip(), options, key=f'g{st.session_state.mq}')
            submit = st.button('Submit')
        if submit:
            st.session_state.mq += 1
            st.session_state.ma.append(ans)
