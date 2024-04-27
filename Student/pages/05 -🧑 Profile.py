import streamlit as st
from PIL import Image
global name
global mood

global experience

# parameters for now, this will come from survey page:
mood = 'Happy'
name = 'Osen'
experience = 999

def main():
    st.title(f"Hello {name}!")
    
    # Load images
    background_image = Image.open("images/background.png")
    if mood == 'Happy':
        cat_image = Image.open("images/cat_happy.png")
    elif mood == 'Amused':
        cat_image = Image.open("images/cat_amused.png")
    elif mood == 'Inspired':
        cat_image = Image.open("images/ccat_inspired.png")
    elif mood == 'Dont Care':
        cat_image = Image.open("images/ccat_dont_care.png")
    elif mood == 'Annoyed':
        cat_image = Image.open("images/ccat_annoyed.png")
    elif mood == 'Afraid':
        cat_image = Image.open("images/ccat_afraid.png")
    elif mood == 'Sad':
        cat_image = Image.open("images/ccat_sad.png")
    elif mood == 'Angry':
        cat_image = Image.open("images/ccat_angry.png")

    
    # Calculate level and remaining experience
    level = experience // 100
    remaining_experience = experience % 100
    
    # Calculate width of level bar based on remaining experience
    level_bar_width = remaining_experience / 100 * 150  # Percentage of 100 pixels
    
    # Display stacked images with text
    st.write(
        f"""
        <div style="position:relative;">
            <img src="data:image/png;base64,{image_to_base64(background_image)}" style="width:100%;">
            <div style="position:absolute;top:0;left:0;padding:30px;color:black;font-size:30px;font-family:inherit;font-weight:bold;">Mood: {mood} | Level: {level}</div>
            <div style="position:absolute;top:75px;left:30px;width:150px;height:20px;background-color:gray;">
                <div style="position:absolute;top:0;left:0;width:{level_bar_width}px;height:20px;background-color:green;"></div>
            </div>
            <img src="data:image/png;base64,{image_to_base64(cat_image)}" style="position:absolute;top:50%;left:50%;transform:translate(-50%, -50%);width:75%">
        </div>
        """,
        unsafe_allow_html=True
    )

def image_to_base64(image):
    import base64
    import io
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

if __name__ == "__main__":
    main()
