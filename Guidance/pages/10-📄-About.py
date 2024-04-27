import streamlit as st

import control_flow as cf

if __name__ == "__main__":

    emoji = ":page_facing_up:"

    st.set_page_config(
        page_title = "About",
        page_icon = emoji,
        initial_sidebar_state = "expanded",
    )

    # Load initial data if it hasn't already been loaded.
    cf.load_initial_data_if_needed()

    st.markdown("(PROJECT TITLE)")
    st.title(f"{emoji} About")

    st.markdown("""The app was developed by...

The following are our sources...

                """)
    
    st.markdown("---")

    st.markdown("""Contact Information
    
- Email: ...
- GitHub: ...
- LinkedIn: ...
                
    """)
    
    cf.display_copyright()