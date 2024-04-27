import streamlit as st


# Welcome
name = 'Val'
st.title(f'Hi {name}. Kumusta ka?')

# Choose survey
st.caption('Answer a wellness survey today.')
options = ['Weekly Well-being', 'Monthly Check-up']
choice = st.radio('What do you want to answer?', options)

# General Health Questionnaire
if choice == options[0]:
    form1 = st.form('General Well-being')

    questions = """Able to concentrate
    Loss of sleep over worry
    Playing a useful part
    Capable of making decisions
    Felt constantly under strain
    Couldn’t overcome difficulties
    Able to enjoy day-to-day activities
    Able to face problems
    Feeling unhappy and depressed
    Losing confidence
    Thinking of self as worthless
    Feeling reasonably happy"""

    st.write('In a scale of 1 to 4, how well do you resonate with the following statements or questions?')
    for i in questions.split('\n'):
        form1.slider(i.strip(), 1,4,1,1)
    form1.form_submit_button('Submit')


# Monthly Check-up
if choice == options[1]:
    form2 = st.form('general_health')

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

    st.write('In a scale of 1 to 7, how well do you resonate with the following statements or questions?')
    for i in questions.split('\n'):
        form2.slider(i.strip(), 1,7,1,1)
    form2.form_submit_button("Submit")
