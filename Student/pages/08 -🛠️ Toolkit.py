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
    if st.button('Listen'):
        nav_page("listen")
    if st.button('Journal'):
        nav_page("journal")


def hide_page(page_name, **kwargs):
    _inject_page_script(page_name, 'link.style.display = "none";', **kwargs)

def show_page(page_name, **kwargs):
    _inject_page_script(page_name, 'link.style.display = "";', **kwargs)

def disable_page(page_name, **kwargs):
    _inject_page_script(page_name, 'link.style.pointerEvents = "none"; '
                                   'link.style.opacity = 0.5;', **kwargs)

def enable_page(page_name, **kwargs):
    _inject_page_script(page_name, 'link.style.pointerEvents = ""; '
                                   'link.style.opacity = "";', **kwargs)

def _inject_page_script(page_name, action_script, timeout_secs=3):
    page_script = """
        <script type="text/javascript">
            function attempt_exec_page_action(page_name, start_time, timeout_secs, action_fn) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        action_fn(links[i]);
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_exec_page_action, 100, page_name, start_time, timeout_secs, action_fn);
                } else {
                    alert("Unable to locate link to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_exec_page_action("%s", new Date(), %d, function(link) {
                    %s
                });
            });
        </script>
    """ % (page_name, timeout_secs, action_script)
    html(page_script, height=0)

hide_page("study")
hide_page("test")
hide_page("listen")
hide_page("meditate")
hide_page("journal")