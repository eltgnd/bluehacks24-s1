import streamlit as st
import random as rand
import os 
try:
    from pytube import Playlist, YouTube
    from art import *
except ModuleNotFoundError:
    os.system('pip install pytube')
    os.system('pip install art')

def get_playlist(playlists):
    urls = []

    for playlist in playlists:
        playlist_urls = Playlist(playlist)

        for url in playlist_urls:
            urls.append(url)

    return urls

playlist = ['https://www.youtube.com/watch?v=9TXgKPSLxIY&list=PLW8o3_GFoCBNWV3KtiiXNsg3zDgZqEyFf&ab_channel=Headspace']
pl_urls = get_playlist(playlist)

st.title("Meditation of the Day")

rng = rand.randint(1,len(pl_urls))
url = pl_urls[rng]
st.subheader(f'{YouTube(url).title}')
st.video(url)

col1, col2, col3, col4, col5 = st.columns([0.2, 1,1,1, 0.2])
with col2:
    st.write(f'**Views:** {YouTube(url).views}')
with col3:    
    st.write(f'**Channel:** {YouTube(url).author}')
with col4:
    st.write(f'**Publish Date:** {YouTube(url).publish_date.date()}')

