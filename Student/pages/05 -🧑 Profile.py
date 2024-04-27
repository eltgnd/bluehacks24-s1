import streamlit as st
import plotly.express as px
from streamlit_gsheets import GSheetsConnection
from PIL import Image

# global experience

# Google Sheets Connection
conn = st.connection("survey", type=GSheetsConnection)

# Parameters for now, this will come from survey page:
mood = 'Happy'
name = 'Osen'
experience = 999

# Title
st.title(f'Welcome {st.session_state.name}! 👋')
st.write(f'Student ID: {st.session_state.student_id}')

# Daily Survey
# with st.container(border=True):
#     sql = f'SELECT Mood,Date FROM Sheet1 WHERE "Student ID" = {st.session_state.student_id} ORDER BY Date;'
#     df = conn.query(sql=sql, ttl=0)

#     fig = px.bar(df, x='Date', y='Mood', title='Mood Over Time')
#     st.plotly_chart(fig)


# General Survey
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

with st.container(border=True):
    sql = f'SELECT "General Survey",Date FROM Sheet1 WHERE "Student ID" = {st.session_state.student_id} ORDER BY Date;'
    df = conn.query(sql=sql, ttl=0)

    for i in range(12):
        df[i] = df['General Survey'].str[1:-1].str.split(',').str[i]
    option = st.selectbox('General Wellbeing', question_lst, index=None)
    if option:
        ind = question_lst.index(option)
        filtered_df = df[['Date', ind]]

        fig = px.line(df, x='Date', y=ind, title='Response History')
        fig.update_traces(line=dict(width=2, color='DarkSlateGrey'))

        # Customize layout
        # fig.update_layout(
        #     autosize=False,
        #     width=500,
        #     height=500,
        #     margin=dict(l=50, r=50, b=100, t=100, pad=4),
        #     paper_bgcolor="LightSteelBlue",
        # )
        st.plotly_chart(fig, use_container_width=True)




