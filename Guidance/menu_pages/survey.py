import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from PIL import Image

def turn_int(x):
    return int(x)

# Google Sheets Connection
conn = st.connection("survey", type=GSheetsConnection)

# Title
st.caption('BUGHAW   |   GUIDANCE COUNSELORS\' PORTAL')
st.title(f'Welcome {st.session_state.name}! 👋')
st.markdown("""
    View descriptive analytics from student-provided data.
""")

# Weekly Survey
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

with st.expander('Weekly Wellbeing'):
    sql = f"""SELECT "General Survey",Date FROM Sheet1;"""
    df = conn.query(sql=sql, ttl=0)

    for i in range(12):
        df[i] = df['General Survey'].str[1:-1].str.split(',').str[i]
        df[i] = df[i].apply(turn_int)

    # Compute statistics

    df['Date'] = pd.to_datetime(df['Date'])
    df.drop(columns=['General Survey'], inplace=True)
    # Group by weeks
    weekly = df.groupby(pd.Grouper(key='Date', freq='W'))
    # Calculate different descriptive statistics
    weekly_mean = weekly.mean()
    weekly_median = weekly.median()
    weekly_std = weekly.std()
    func_lst = [weekly_mean, weekly_median, weekly_std]

    option = st.selectbox('', question_lst, index=None)
    if option:
        ind = question_lst.index(option)
        # mean pa lang to
        weekly_mean = weekly_mean.reset_index()
        filtered_df = weekly_mean[['Date', ind]]
        fig = px.line(filtered_df, x='Date', y=ind, title='')
        fig.update_traces(line=dict(width=2, color='DarkSlateGrey'))
        fig.update_xaxes(tickvals=filtered_df['Date'])
        st.plotly_chart(fig, use_container_width=True)

# Monthly Survey
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

with st.expander('Monthly Wellbeing'):
    sql = f"""SELECT "Monthly Survey",Date FROM Sheet1 ORDER BY Date;"""
    df = conn.query(sql=sql, ttl=0)

    for i in range(12):
        df[i] = df['Monthly Survey'].str[1:-1].str.split(',').str[i]
        df[i] = df[i].apply(turn_int)

    # Compute statistics

    df['Date'] = pd.to_datetime(df['Date'])
    df.drop(columns=['Monthly Survey'], inplace=True)
    # Group by Months
    monthly = df.groupby(pd.Grouper(key='Date', freq='M'))
    # Calculate different descriptive statistics
    monthly_mean = monthly.mean()
    monthly_median = monthly.median()
    monthly_std = monthly.std()
    func_lst = [monthly_mean, monthly_median, monthly_std]

    option = st.selectbox('', question_lst, index=None)
    if option:
        ind = question_lst.index(option)
        # mean pa lang to
        monthly_mean = monthly_mean.reset_index()
        filtered_df = monthly_mean[['Date', ind]]
        fig = px.line(filtered_df, x='Date', y=ind, title='')
        fig.update_traces(line=dict(width=2, color='DarkSlateGrey'))
        fig.update_xaxes(tickvals=filtered_df['Date'])
        st.plotly_chart(fig, use_container_width=True)