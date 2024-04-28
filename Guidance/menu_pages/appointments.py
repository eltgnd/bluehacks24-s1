import streamlit as st
import control_flow as cf
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import streamlit.components.v1 as components
from datetime import datetime
import calendar

# Initialize counselors
counselors = {'g001' : 'counselor_1_calendar', 'g002' : 'counselor_2_calendar'}

@st.cache_resource(ttl=0, max_entries = 1)
def connect_to_database():
    """
    Connects to the appointments database.
    """
    conn = st.connection("appointments", type=GSheetsConnection)
    return conn

def reformat_datetime(datetime_string):
    """
    Reformats a datetime string returned by the appointments form
    to a form that can be compared via if-else statements.
    """
    splitted_info = datetime_string.split()
    day = splitted_info[0].replace(',', '')
    month = splitted_info[1]
    date = splitted_info[2].replace(',', '')
    year = splitted_info[3]
    start_time = splitted_info[4].split('-')[0]
    end_time = splitted_info[4].split('-')[0]
    splitted_info = [day, month, date, year, start_time, end_time]
    
    dt = datetime.strptime(f'{year}-{month}-{date} {end_time}', '%Y-%b-%d %H:%M')
    return dt

if __name__ == "__main__":
    # Page symbol
    emoji = ":page_facing_up:"
   
    # Page links
    st.set_page_config(
        page_title = "Appointments",
        page_icon = emoji,
        initial_sidebar_state = "auto",  
    )

    # Load initial data if it hasn't already been loaded.
    cf.load_initial_data_if_needed()

    counselor_1_calendar = "https://calendar.google.com/calendar/embed?src=c_54806ee2c0fb06874da21a8fc5346db6178df6e7396ef9e6fa00bc6a3e79f4c6%40group.calendar.google.com&ctz=Asia%2FManila"
    counselor_2_calendar = "https://calendar.google.com/calendar/embed?src=c_f4ee311db2f27dac7f7933d508a288429e4961b57eede8f2ed4ab00bd3084e76%40group.calendar.google.com&ctz=Asia%2FManila"
    calendars = ['counselor_1_calendar', 
                 'counselor_2_calendar']
 
    # Caption
    st.caption('BUGHAW   |   GUIDANCE COUNSELORS\' PORTAL')
    st.title(f"{emoji} Appointments")
    
    # ---------
    conn = connect_to_database()
    dt_now = datetime.now() # Obtain date and time now

    st.markdown(f"""
    ## Hello, {st.session_state.name}!

    This page contains your past and upcoming appointments.

    """)

    # Select the appointment calendar specific to the guidance counselor
    # by checking the calendars array for the user_id of the guidance counselor
    # as a substring
    # Reference: [wait nawawala]
    selected_calendar = [calendar for calendar in calendars if 
                         counselors[st.session_state.counselor_id] == calendar][0]

   # Different views for the selectbox
   # Select is default/placeholder
    views = ['Select', 'Calendar', 'List']

    views = st.selectbox(
        "Appointment Views",
        views
    )

    if views == 'Calendar':
             components.iframe(globals()[selected_calendar], scrolling=True, height=500)
        
    elif views == 'List':
        # Query the appointments calendar of the guidance counselor logged in.
        sql = f"""SELECT {selected_calendar} AS Schedule, username AS Username, anonymous AS Anonymous, online_or_onsite AS 'Online or Onsite?' FROM appointments;"""
        
        df = conn.query(sql=sql).dropna(how='any') # Drop empties
        df['date_modified'] = df['Schedule'].apply(reformat_datetime) # Reformat the appointment schedules to a format we can use for comparison
        
        st.write("Select what you want to view.")

        past = st.toggle('Past Appointments', key='past')
        if past:
            # Show past appointments
            df1 = df[df['date_modified'] <= dt_now]
            st.dataframe(df1[['Schedule', 'Username', 'Anonymous', 'Online or Onsite?']])

        upcoming = st.toggle('Upcoming Appointments', key='upcoming')
        if upcoming:
            # Show upcoming appointments
            df2 = df[df['date_modified'] >= dt_now]
            st.dataframe(df2[['Schedule', 'Username', 'Anonymous', 'Online or Onsite?']])

    # ---------
    
    cf.display_copyright()