import location
import streamlit as st
import os
import download_audio
from location import get_rand_lat_long
import config
import requests
import pandas as pd
import numpy as np


# Function to display the audio files
def audio_calls():
    download_audio.download()
    path = './data/'

    st.header(":phone: Live Call Dashboard")
    i = 0
    for filename in os.listdir(path):
        with st.beta_expander(filename):
            col1, col2 = st.beta_columns(2)
            audio_file = open(path + filename, 'rb')
            audio_bytes = audio_file.read()
            col1.audio(audio_bytes, format='audio / wav')
            col2.button(filename)
        i += 1
    return

def audio_uploader():
    uploaded_file = st.file_uploader("Choose a file")


def location_services():
    df = pd.read_csv('911.csv')
    df_latlong = df[['lat', 'lng']]
    index = np.random.randint(0, 663522)
    latitude = df_latlong.loc[index].lat
    longitude = df_latlong.loc[index].lng
    key = "AIzaSyBWyJXeBhUSMuu9dB7YlMIXFlY0zlr37vg"
    response = requests.get(
        f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={key}")
    address = response.json()
    st.write(address["results"][0]["formatted_address"])
    return address["results"][0]["formatted_address"]


# Function to display menu once logged in
def login_menu():
    st.sidebar.header(":gear:  Services")
    choice = st.sidebar.radio("Menu",
                              ["Incoming Calls", "Call Transcripts", "Summarized Report", "Dashboard",
                               "Notify Entities"])

    if choice == "Incoming Calls":
        audio_calls()

    elif choice == "Call Transcripts":
        uploaded_file = st.file_uploader("Choose a file", help="Upload a call recording (wav/mp3) to get the transcript")
        if uploaded_file is not None:
            audio_bytes = uploaded_file.read()
            st.audio(audio_bytes, format='audio / wav')

    elif choice == "Summarized Report":
        st.write("WIP")

    elif choice == "Dashboard":
        st.write("WIP")

    elif choice == "Notify Entities":
        lat, long, address = location.get_address()
        st.success("Emergency Location: "+address)

        choice = st.selectbox(label="Search", options=['Hospitals', 'Police', 'Fire'], index=0, help="Select to get Emergency Services nearby victim's location")
        if st.button("Search"):
            if choice == "Hospitals":
                location.get_hospitals(lat, long)
            elif choice == "Police":
                location.get_police(lat, long)
            elif choice == "Fire":
                location.get_fire_dept(lat, long)

        st.markdown(f"""
           <iframe width="1050" height="850" frameborder="0" style="border:0" src="https://www.google.com/maps/embed/v1/place?key=AIzaSyBWyJXeBhUSMuu9dB7YlMIXFlY0zlr37vg&q=Lower+Gwynedd+Functional+Medicine&center=40.1868803,-75.22660809999999&zoom=18&maptype=satellite" allowfullscreen></iframe>
           """, unsafe_allow_html=True)
    return
