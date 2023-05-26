import streamlit as st
import requests
import bs4
import time
from streamlit_option_menu import option_menu
st.title("")
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options = ["Home","MI vs GT","Live Streaming"],
    )
if selected == "Home":
    st.title("Live Score Update Faster then your expectations")
if selected=="Live Streaming":
        movie_url = 'https://www.jiocinema.com/sports'
        st.header('Watch Online Streaming')
        st.markdown(f'<iframe src="{movie_url}" width="800" height="600" frameborder="0" allowfullscreen></iframe>',
            unsafe_allow_html=True)
if selected=="MI vs GT":


    st.title("Match Updates")

    # Placeholder for Match Info
    match_info_placeholder = st.empty()

    link = 'https://www.cricketworld.com/cricket/gujarat-titans-vs-mumbai-indians/match/live/62446'

    while True:

        if selected == "Live Streaming":
               break
        elif selected == "Home":
            break
        res = requests.get(link)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        match_info = []
        match_details = soup.select('.match-header')
        for detail in match_details:
            match_info.append(detail.text)
        match_info_placeholder.header("Match Info")
        for info in match_info:
            match_info_placeholder.write(info)
        time.sleep(5)



