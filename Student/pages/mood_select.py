import streamlit as st
from streamlit_image_select import image_select
from PIL import Image

global mood

def main():
    st.title("Selet your mood for today!")
    st.write("Select your mood for today by clicking on the corresponding image:")
    mood = ["Happy", "Amused", "Inspired", "Don't Care", "Annoyed", "Afraid", "Sad", "Angry"]

    # Display mood images and get user input
    selected_mood = image_select(label="", images=["images/8_happy.png", "images/7_amused.png", 
                                                   "images/6_inspired.png", "images/5_dont_care.png",
                                                   "images/4_annoyed.png", "images/3_afraid.png",
                                                   "images/2_sad.png", "images/1_angry.png"], 
                                                   use_container_width=False,
                                                   captions=["Happy", "Amused", "Inspired", "Don't Care",
                                                             "Annoyed", "Afraid", "Sad", "Angry"],
                                                    return_value="index")
    mood = mood[int(str(selected_mood)[:100])]

if __name__ == "__main__":
    main()
