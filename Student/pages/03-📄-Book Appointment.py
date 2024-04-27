import streamlit as st
import control_flow as cf
import streamlit.components.v1 as components


if __name__ == "__main__":
    
    # Page symbol
    emoji = ":page_facing_up:"

    # Important links
    form = "https://form.jotform.com/241171959843465"
    counselor_1_calendar = "https://calendar.google.com/calendar/embed?src=c_54806ee2c0fb06874da21a8fc5346db6178df6e7396ef9e6fa00bc6a3e79f4c6%40group.calendar.google.com&ctz=Asia%2FManila"
    counselor_2_calendar = "https://calendar.google.com/calendar/embed?src=c_f4ee311db2f27dac7f7933d508a288429e4961b57eede8f2ed4ab00bd3084e76%40group.calendar.google.com&ctz=Asia%2FManila"
    
    # Page links
    st.set_page_config(
        page_title = "Book an Appointment",
        page_icon = emoji,
        initial_sidebar_state = "auto", # initially closed 
    )

    # Load initial data if it hasn't already been loaded.
    cf.load_initial_data_if_needed()

    st.markdown("(PROJECT TITLE)") # Name of our project will be displayed in small text above the current page title.
    st.title(f"{emoji} Book an Appointment")

    # ---------

    # Instructions for booking
    st.markdown("""
    ## Instructions
    
    
    To set an appointment with your guidance counselor,
    1. **Check their availability below.**
    """)

    # Select box for counselor
    # Displays the selected counselor's calendar
    counselors = ['Counselor 1', 'Counselor 2']
    options = st.selectbox(
        'Which counselor\'s schedule do you want to view?',
        counselors,
        key = 'selected_counselor'
    )

    if st.session_state.selected_counselor == 'Counselor 1':
        components.iframe(counselor_1_calendar, scrolling=True, height=500)

    elif st.session_state.selected_counselor == 'Counselor 2':
        components.iframe(counselor_2_calendar, scrolling=True, height=500)

    
    st.markdown("""
    2. Once you have picked who you want to talk to and when,
    fill up the form below. ***Note that it only asks for your username, and you have the option
    to remain anonymous if you want!***
    
    3. **Each consultation is for 30 minutes.** You may opt to talk online or offline. If you want your
    information to remain anonymous, the consultation will default to an online setup.
    """)

    # Display form
    st.markdown("## Appointment Form")
    components.iframe(form, scrolling=True, height=500)
    
    ## Add functionality na may prompt sa baba after they are done submitting the form

    # ---------
    
    cf.display_copyright()