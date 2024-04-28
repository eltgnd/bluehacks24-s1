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
st.write('Welcome to the Toolkit page! Here, you\'ll find a range of resources designed to help you build a personalized mental wellness toolkit. Whether you\'re looking for relaxation techniques, stress management strategies, or self-care practices, we\'ve got you covered. Explore our selection of tools, including journaling prompts, guided meditations, and coping skills exercises, all aimed at promoting your mental well-being. Empower yourself to take charge of your mental health journey and discover techniques that resonate with you. Your toolkit is your go-to resource for cultivating resilience and finding balance in your everyday life.')
st.divider()

# Assuming mood and mood_list are defined elsewhere
mood = st.session_state['mood']
mood_list = ["Happy", "Amused", "Inspired", "Don't Care", "Annoyed", "Afraid", "Sad", "Angry"]
path = ['happy', 'amused', 'inspired', 'dont_care', 'annoyed', 'afraid', 'sad', 'angry']
pos = mood_list.index(mood)

image_path = f"Student/images/profile_{path[pos]}.png" 
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
    st.write('Study 💡: Explore our Study page to learn techniques for managing emotions like annoyance, fear, sadness, anger, and stress. Empower yourself with strategies to enhance your emotional well-being.')
    st.write('Meditate 🧘: Find peace and relaxation on our Meditate page. Watch guided meditation videos to calm your mind, reduce stress, and cultivate mindfulness.')
    st.write('Read 📚: Stay informed about mental health with our Read page. Access the latest news and articles covering important topics and insights into well-being.')

#Read 📚: Immerse yourself in a world of knowledge and inspiration with our Read page. Discover a curated collection of articles, blogs, and resources on mental health, self-care, and personal development. From expert insights to real-life stories, there's something for everyone to explore. Expand your mind, gain new perspectives, and empower yourself with the wisdom found within the pages of our Read section. 📖🌟')

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