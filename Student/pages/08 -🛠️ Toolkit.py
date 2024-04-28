import streamlit as st
from streamlit_image_select import image_select
from PIL import Image
from streamlit.components.v1 import html

st.title("Toolkit")

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
col1, col2, col3, col4, col5 = st.columns([2, 30, 30, 30, 32])
with col1:
    st.image(image, width =300)

# Displaying buttons on the right
with col5:
    if st.button('Study'):
        nav_page("study")
    if st.button('Meditate'):
        nav_page("meditate")
    if st.button('Read'):
        nav_page("read")
    if st.button('Journal'):
        nav_page("journal")