import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_image_select import image_select
from PIL import Image
import datetime

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
        st.session_state.ma if survey_type=='m' else None,
        st.session_state.mood if survey_type=='d' else None
    ]

    conn.update(worksheet="Sheet1", data=df)
    st.success("Worksheet Updated! 🥳")

def check_streak():
    sql = f"""SELECT Date FROM Sheet1 WHERE "Student ID"='{st.session_state.student_id}' ORDER BY Date;"""
    df = conn.query(sql=sql)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date_Diff'] = df['Date'].diff().dt.days
    df['Streak_ID'] = (df['Date_Diff'] > 1).cumsum()
    streaks = df.groupby('Streak_ID').cumcount() + 1

    return streaks.max()


# Title
st.caption('BUGHAW   |   STUDENTS\' PORTAL')

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
    options = ['Daily Wellbeing','Weekly Wellbeing', 'Monthly Wellbeing']
    choice = st.radio('What do you want to answer?', options)

# Daily
st.session_state.mood_button = False
if choice == options[0]:
    with st.container(border=True):
        st.write("🌱 Selet your mood for today by clicking on the corresponding image.")
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


# General Health Questionnaire
if choice == options[1]:

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
    if st.session_state.gq > 11:
        st.write('Successfully submitted!')
        st.session_state.submitted_g = True
        update_data('g')
    else:
        with st.container(border=True):
            st.caption(f'Question {st.session_state.gq + 1} of 12')
            ans = st.radio(question_lst[st.session_state.gq].strip(), options, horizontal=True, key=f'g{st.session_state.gq}')
            submit = st.button('Submit')

        if submit:
            st.session_state.gq += 1
            st.session_state.ga.append(int(ans))

# Monthly Check-up
if choice == options[2]:

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
    if st.session_state.gq > 12:
        st.write('Successfully submitted!')
        st.session_state.submitted_m = True
        update_data('m')

    else:
        with st.container(border=True):
            st.caption(f'Question {st.session_state.mq} of 13')
            ans = st.radio(question_lst[st.session_state.mq].strip(), options, key=f'g{st.session_state.mq}')
            submit = st.button('Submit')
        if submit:
            st.session_state.mq += 1
            st.session_state.ma.append(int(ans))