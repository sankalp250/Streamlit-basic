#python  -m streamlit run files.py
import streamlit as st
import pandas as pd
st.subheader('Loading the csv file')
df = st.file_uploader("Upload the csv file: ",type = ['csv','xlsx','png'])

#if df is not None: #--  IT SHOWS THE VALUE 
 #st.dataframe(df)
 
st.subheader('Loading the CSV File')
df = pd.read_csv("Products.csv")
if df is not None:
    st.table(df.head())
    
st.subheader('Working with Images')
st.image("img.png")

st.subheader("dealing with the images while uploading ")
img_file = st.file_uploader("Upload the image file: ", type = ['png','jpeg'])
if img_file is not None:
    st.image(img_file)

st.subheader("working with video file")
video_file = st.file_uploader("Upload the video file: ", type = ["mkv" , "mp4"])
if video_file is not None:
    st.video(video_file, start_time = 0)
    
st.subheader("working with audio file")
audio_file = st.file_uploader("upload the audio file: ", type = ['mp3','wav'])
if audio_file is not None:
    st.audio(audio_file, start_time = 0)

