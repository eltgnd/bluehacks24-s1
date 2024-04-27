import streamlit as st

st.title("Release the tension...")

# Define the options
options = ["Annoyance", "Fear", "Sadness", "Anger", "Stress"]

# Create a dropdown menu
selected_option = st.selectbox('What do you want to reduce?',options)

if selected_option == 'Annoyance':
    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("images/A1.png", width=150)
    with col2:
        st.markdown("""
        <h2>Practice Empathy:</h2>
        
        Try to understand the perspective of the person or situation causing annoyance. 
        Putting yourself in their shoes can help you see things from a different angle 
        and reduce irritation.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("images/A2.png", width=150)
    with col2:
        st.markdown("""
        <h2>Take Deep Breaths</h2>
        
        Use deep breathing exercises to calm your nerves and regain composure. Inhale deeply through your nose, hold for a few seconds, and then exhale slowly through your mouth.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("images/A3.png", width=150)
    with col2:
        st.markdown("""
        <h2>Reframe Your Thoughts </h2>
        Instead of dwelling on the annoyance, try to reframe the situation in a more positive light. Focus on what you can control and let go of what you cannot.

        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("images/A4.png", width=150)
    with col2:
        st.markdown("""
        <h2>Distract Yourself</h2>
Engage in activities or hobbies that shift your focus away from the source of annoyance. Immersing yourself in something enjoyable can help alleviate irritation.

        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("images/A5.png", width=150)
    with col2:
        st.markdown("""
        <h2>Communicate Effectively</h2>
If the annoyance stems from interactions with others, communicate your feelings calmly and assertively. Expressing your concerns respectfully can help address the issue and prevent future annoyances.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("images/A6.png", width=150)
    with col2:
        st.markdown("""
        <h2>Practice Gratitude</h2>
Take a moment to reflect on the positive aspects of your life and express gratitude for them. Shifting your focus to what you're thankful for can help put minor annoyances into perspective.
        """, unsafe_allow_html=True)

elif selected_option == 'Fear':
    pass