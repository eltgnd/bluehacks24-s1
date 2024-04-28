import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from PIL import Image

def turn_int(x):
    return int(x)

# Page config
st.set_page_config(page_title='Data Analytics', page_icon='📊', layout="centered", initial_sidebar_state="auto", menu_items=None)

# Google Sheets Connection
conn = st.connection("survey", type=GSheetsConnection)

# Title
st.caption('BUGHAW   |   GUIDANCE COUNSELORS\' PORTAL')
st.title(f'Welcome {st.session_state.name}! 👋')
st.markdown("""
    Welcome to the Data Analytics section, where counselors gain valuable insights into students' survey data to inform policy decisions and program development. Here, you'll find a comprehensive overview of survey results, aggregated and categorized based on various metrics such as demographics and time periods. Use this data to identify trends, understand student needs, and tailor interventions effectively. Your data-driven approach plays a vital role in promoting student well-being and fostering a supportive learning environment. Together, let's harness the power of information to create positive change.        
    
    Choose a question and *then* choose a descriptive statistic.
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
    sql = f"""SELECT "General Survey", Date FROM Sheet1;"""
    df = conn.query(sql=sql, ttl=0).dropna(how='any')
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
    func_lst = ['mean', 'median', 'stdev']

    option_weekly = st.selectbox('', question_lst, index=None, placeholder='Choose a question', key="option_weekly")
    descriptive_stat_weekly = st.radio('Choose a descriptive statistic', func_lst, index=None, key="descriptive_stat_weekly")
    to_plot_weekly = None

    if option_weekly is not None:
        question_ind = question_lst.index(option_weekly)

        if descriptive_stat_weekly == 'mean':
            to_plot_weekly = weekly_mean
        elif descriptive_stat_weekly == 'median':
            to_plot_weekly = weekly_median
        elif descriptive_stat_weekly == 'stdev':
            to_plot_weekly = weekly_std
        
        if to_plot_weekly is not None:
            to_plot_weekly = to_plot_weekly.reset_index()
            filtered_df = to_plot_weekly[['Date', question_ind]]
            fig = px.line(filtered_df, x='Date', y=question_ind, title=descriptive_stat_weekly,)
            fig.update_traces(line=dict(width=2, color='DarkSlateGrey'))
            fig.update_xaxes(tickvals=filtered_df['Date'])
            fig.update_layout(
                yaxis_title="Response Value",
                title=f'Question {question_ind}: {descriptive_stat_weekly} weekly response values'
            )
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
    sql = f"""SELECT "Monthly Survey", Date FROM Sheet1 ORDER BY Date;"""
    df = conn.query(sql=sql, ttl=0).dropna(how='any')

    for i in range(13):
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
    func_lst = ['mean', 'median', 'stdev']

    option_monthly = st.selectbox('', question_lst, index=None, placeholder='Choose a question', key='option_monthly')
    descriptive_stat_monthly = st.radio('Choose a descriptive statistic', func_lst, index=None, key="descriptive_stat_monthly")
    to_plot_monthly = None

    if option_monthly is not None:
        question_ind = question_lst.index(option_monthly)

        if descriptive_stat_monthly == 'mean':
            to_plot_monthly = monthly_mean
        elif descriptive_stat_monthly == 'median':
            to_plot_monthly = monthly_median
        elif descriptive_stat_monthly == 'stdev':
            to_plot_monthly = monthly_std
        
        if to_plot_monthly is not None:
            to_plot_monthly = to_plot_monthly.reset_index()
            filtered_df = to_plot_monthly[['Date', question_ind]]
            fig = px.line(filtered_df, x='Date', y=question_ind, title=descriptive_stat_monthly)
            fig.update_traces(line=dict(width=2, color='DarkSlateGrey'))
            fig.update_xaxes(tickvals=filtered_df['Date'])
            fig.update_layout(
                yaxis_title="Response Value",
                title=f'Question {question_ind}: {descriptive_stat_monthly} monthly response values'
            )
            st.plotly_chart(fig, use_container_width=True)