import streamlit as st
from streamlit_image_select import image_select
from st_pages import Page, Section,show_pages, add_page_title, hide_pages
from PIL import Image
from streamlit.components.v1 import html

st.set_page_config(
    page_title = f'{st.session_state.name}\'s Toolkit',
    page_icon = "🛠️",
    initial_sidebar_state = "expanded",
)
# Title
st.title(f"🛠️ {st.session_state.name}\'s Toolkit")
st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.')
st.divider()

# Assuming mood and mood_list are defined elsewhere
mood = st.session_state['mood']
mood_list = ["Happy", "Amused", "Inspired", "Don't Care", "Annoyed", "Afraid", "Sad", "Angry"]
path = ['happy', 'amused', 'inspired', 'dont_care', 'annoyed', 'afraid', 'sad', 'angry']
pos = mood_list.index(mood)

image_path = f"images/profile_{path[pos]}.png" 
image  = Image.open(image_path)

def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)


def image_to_base64(image):
    import base64
    import io
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Displaying the image on the left
col1, col2 = st.columns([20,30])

with col1:
    st.write('💡 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.')

# Displaying buttons on the right
with col2:
    st.image(image, width=400)

    s0, s1, s2, s3, s4 = st.columns([2,8,10,8,3], gap='small')
    with s1:
        if st.button('Study 💡'):
            nav_page("study")
    with s2:
        if st.button('Meditate 🧘'):
            nav_page("meditate")
    with s3:
        if st.button('Read 📚'):
            nav_page("read")

st.divider()