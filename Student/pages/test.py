import streamlit as st

# Define a variable to track the visibility of the page
show_page = st.session_state.get("show_page", False)

# Create a button in the sidebar to reveal the page
show_button = st.sidebar.button("Show Hidden Page")

# Update the visibility variable based on button click
if show_button:
    show_page = True

# Display the page content if it's visible
if show_page:
    st.title("Hidden Page")
    st.write("This is a hidden page. You can access it by clicking the button in the sidebar.")
