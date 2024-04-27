import streamlit as st
from PIL import Image
from Home import *

def main():
    st.title("🧑 Profile")
    st.write(f'Hello {name}!')
    st.write(f'Current Mode: {mood}')
    st.write(f'Current Level: {experience//100}!')

    #@Val write statistics here:
    profile_sidebar()

if __name__ == "__main__":
    main()
