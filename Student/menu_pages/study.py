import streamlit as st

st.set_page_config(
    page_title = "Release the tension...",
    page_icon = "🧠",
    initial_sidebar_state = "expanded",
)

st.title("Release the tension...")

# Define the options
options = ["-", "Annoyance", "Fear", "Sadness", "Anger", "Stress"]

# Create a dropdown menu
selected_option = st.selectbox('What do you want to reduce?',options)

if selected_option == 'Annoyance':
    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/A1.png", width=150)
    with col2:
        st.markdown("""
        <h2>Practice Empathy</h2>
        
        Try to understand the perspective of the person or situation causing annoyance. 
        Putting yourself in their shoes can help you see things from a different angle 
        and reduce irritation.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/A2.png", width=150)
    with col2:
        st.markdown("""
        <h2>Take Deep Breaths</h2>
        
        Use deep breathing exercises to calm your nerves and regain composure. Inhale deeply through your nose, hold for a few seconds, and then exhale slowly through your mouth.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/A3.png", width=150)
    with col2:
        st.markdown("""
        <h2>Reframe Your Thoughts </h2>
        Instead of dwelling on the annoyance, try to reframe the situation in a more positive light. Focus on what you can control and let go of what you cannot.

        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/A4.png", width=150)
    with col2:
        st.markdown("""
        <h2>Distract Yourself</h2>
Engage in activities or hobbies that shift your focus away from the source of annoyance. Immersing yourself in something enjoyable can help alleviate irritation.

        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/A5.png", width=150)
    with col2:
        st.markdown("""
        <h2>Communicate Effectively</h2>
If the annoyance stems from interactions with others, communicate your feelings calmly and assertively. Expressing your concerns respectfully can help address the issue and prevent future annoyances.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/A6.png", width=150)
    with col2:
        st.markdown("""
        <h2>Practice Gratitude</h2>
Take a moment to reflect on the positive aspects of your life and express gratitude for them. Shifting your focus to what you're thankful for can help put minor annoyances into perspective.
        """, unsafe_allow_html=True)

elif selected_option == 'Fear':
    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/B1.png", width=150)
    with col2:
        st.markdown("""
        <h2>Deep Breathing</h2>
        
        Take slow, deep breaths to calm your body and mind. Inhale deeply through your nose, hold for a few seconds, and then exhale slowly through your mouth.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/B2.png", width=150)
    with col2:
        st.markdown("""
        <h2>Positive Affirmations</h2>
        Use positive self-talk to counteract fearful thoughts. Repeat affirmations such as "I am strong," "I am capable," or "I can handle this" to boost your confidence.""", unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/B3.png", width=150)
    with col2:
        st.markdown("""
        <h2>Positive Affirmations</h2>
       Imagine yourself successfully overcoming the source of your fear. Visualize a positive outcome and focus on how it would feel to conquer your fears.
    
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/B4.png", width=150)
    with col2:
        st.markdown("""
        <h2>Break It Down</h2>
    Break the situation or task that triggers fear into smaller, more manageable steps. Focus on tackling one step at a time, gradually building momentum and confidence.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/B5.png", width=150)
    with col2:
        st.markdown("""
        <h2>Seek Support</h2>
        Reach out to friends, family, or a trusted mentor for encouragement and reassurance. Sharing your fears with someone supportive can provide comfort and perspective.
        """, unsafe_allow_html=True)
    st.write('\n')

    
    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/B6.png", width=150)
    with col2:
        st.markdown("""
        <h2>Take Action</h2>
        Face your fears head-on by taking proactive steps to confront them. Each small action you take toward overcoming your fears will help build courage and resilience over time.
        """, unsafe_allow_html=True)
    st.write('\n')


elif selected_option == 'Sadness':
    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/C1.png", width=150)
    with col2:
        st.markdown("""
        <h2>Engage in Physical Activity</h2>
        Get moving by going for a walk, doing some yoga, or even dancing to your favorite music. Physical activity releases endorphins, which are natural mood lifters.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/C2.png", width=150)
    with col2:
        st.markdown("""
        <h2>Get Adequate Sleep</h2>
        Make sure you're getting enough restful sleep each night. Aim for 7-9 hours of quality sleep to help improve your mood and overall well-being.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/C3.png", width=150)
    with col2:
        st.markdown("""
        <h2>Practice Gratitude</h2>
        Take a few moments each day to write down or think about things you're grateful for. Focusing on the positive aspects of your life can help shift your perspective and reduce feelings of sadness.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/C4.png", width=150)
    with col2:
        st.markdown("""
        <h2>Connect with Loved Ones</h2>
        Reach out to friends or family members for support. Talking to someone you trust about how you're feeling can provide comfort and reassurance.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/C5.png", width=150)
    with col2:
        st.markdown("""
        <h2>Limit Media Consumption</h2>
        Reduce exposure to negative news or social media if it's contributing to your sadness. Instead, try engaging in activities that uplift and inspire you.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/C6.png", width=150)
    with col2:
        st.markdown("""
        <h2>Seek Professional Help</h2>
        If sadness persists or interferes with your daily life, consider talking to a therapist or counselor. They can provide guidance, support, and strategies to help you cope with and overcome your feelings of sadness.
        """, unsafe_allow_html=True)
    st.write('\n')


elif selected_option == 'Anger':
    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/D1.png", width=150)
    with col2:
        st.markdown("""
        <h2>Breathe</h2>
        Finding a quiet spot and focus on your breathing.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/D2.png", width=150)
    with col2:
        st.markdown("""
        <h2>Find Alignment</h2>
        Stand with your feet a short distance apart from each other. Make sure they line up with your hips and to bend your knees slightlight. Dig your feet and toes into it.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/D3.png", width=150)
    with col2:
        st.markdown("""
        <h2>Ground Yourself</h2>
        Pull your shoulders back and take several slow breaths. With your hands, knead the skin on your arms, neck, and shoulders. Pay attention to the sensations of your body.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/D4.png", width=150)
    with col2:
        st.markdown("""
        <h2>Visualize What Made You Angry</h2>
        Think about the incident that triggered your anger. Picture out all the details until you feel your anger rise.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/D5.png", width=150)
    with col2:
        st.markdown("""
        <h2>Check for Feelings Other Than Anger</h2>
        It’s helpful to name your feelings out loud, one at a time. This can be “I am hurt,” “I feel embarrassed,” “I am heartbroken,” “I feel anxious,” “I am scared,” or “I am ambivalent.”
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/D6.png", width=150)
    with col2:
        st.markdown("""
        <h2>Journal Your Experience</h2>
        Write down your experience. You may start with “It’s safe to be present in my body. It’s safe to feel my feelings.” Explore your emotions as you write these.
        """, unsafe_allow_html=True)
    st.write('\n')
    
elif selected_option == 'Stress':
    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/E1.png", width=150)
    with col2:
        st.markdown("""
        <h2>Mindfulness Meditation</h2>
        Focus on your breath. Acknowledge and accept the thoughts that pass through your mind.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/E2.png", width=150)
    with col2:
        st.markdown("""
        <h2>Music Meditation</h2>
        Pay attention to the sounds and rhythms of different music pieces. 
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/E3.png", width=150)
    with col2:
        st.markdown("""
        <h2>Body Scan Meditation</h2>
        Slowly direct your attention to different parts of your body, from your toes to your head.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/E4.png", width=150)
    with col2:
        st.markdown("""
        <h2>Mantra Meditation</h2>
        Silently repeat a calming word or phrase (a “mantra”) to yourself to prevent distracting thoughts.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/E5.png", width=150)
    with col2:
        st.markdown("""
        <h2>Walking Meditation</h2>
        Try to walk or move around for a few minutes.
        """, unsafe_allow_html=True)
    st.write('\n')

    col1, col2 = st.columns([1,3])
    with col1:
        image = st.image("Student/images/E6.png", width=150)
    with col2:
        st.markdown("""
        <h2>Loving-Kindness Meditation</h2>
        Send goodwill, kindness, and warmth towards yourself and/or others by silently repeating a series of compassionate phrases. Such as “May you be happy. May you be healthy. May you be at peace.”
        """, unsafe_allow_html=True)
    st.write('\n')