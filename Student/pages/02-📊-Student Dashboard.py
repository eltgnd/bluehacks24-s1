import streamlit as st

def update_gq(ans):
    st.session_state.ga.append(ans)
    st.session_state.gq += 1

    st.write(st.session_state.gq)

    if st.session_state.gq > 12:
        st.session_state.gq = 0

# Welcome
name = st.session_state.name
st.title(f'Hi {name.capitalize()}. 👋 Kumusta ka?')

# Choose survey
with st.container(border=True):
    options = ['Weekly Well-being', 'Monthly Check-up']
    choice = st.radio('What do you want to answer?', options)

# General Health Questionnaire
if choice == options[0]:

    st.session_state.gq = 1
    st.session_state.ga = []

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

    st.write('In a scale of 1 to 4, how well do you resonate with the following statements or questions?')

    # Place question
    gq = st.session_state.gq
    if gq == 0:
        st.write('Successfully submitted!')
    else:
        st.caption(f'Question {gq} of 12')
        ans = st.slider(question_lst[gq].strip(), 1,4,1,1)
        submit = st.button('Submit', on_click=update_gq(ans))

    # for i in range(len(question_lst)):
    #     form = st.form(f'g{i}')
    #     with previous.container():
    #         st.caption(f'Question {i} of 12')
    #         val = form.slider(question_lst[i].strip(), 1,4,1,1)
    #         submitted = form.form_submit_button('Submit')
    #     if submitted:
    #         answers.append(val)
    


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


# View data
# conn = st.connection("survey", type=GSheetsConnection)

# df = conn.read(worksheet = "Sheet1", ttl=0)

