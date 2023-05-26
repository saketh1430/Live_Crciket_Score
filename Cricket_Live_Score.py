import streamlit as st
import requests
import bs4
import time
from streamlit_option_menu import option_menu
st.markdown(
    """
    <style>
    .reportview-container {
        max-width: 100%;
        padding-left: 0px;
        padding-right: 0px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        max-width: 250px;
        padding-left: 10px;
        padding-right: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

hide_footer_style = """
    <style>
    .reportview-container .main footer {
        visibility: hidden;
    }
    """
st.markdown(hide_footer_style, unsafe_allow_html=True)
st.markdown(""" 
<style>
.css-1rs6os.edgvbvh3
{
visibility: hidden;
}
.css-cio0dv.egzxvld1
{
   visibility:hidden;
}
</style>""",unsafe_allow_html= True )
st.title("Match Updates")
match_info_placeholder = st.empty()
Overs_info_placeholder = st.empty()
Commentry_info_placeholder = st.empty()

link = 'https://www.cricketworld.com/cricket/gujarat-titans-vs-mumbai-indians/match/live/62446'
link1 = 'https://crex.live/scoreboard/JPG/19W/Qualifier-2/F/KB/gt-vs-mi-qualifier-2-indian-premier-league-2023/live'


while True:
    res = requests.get(link)
    res1 = requests.get(link1)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    soup1 = bs4.BeautifulSoup(res1.text, 'html.parser')
    match_info = []
    match_details = soup.select('.match-header')
    for detail in match_details:
        match_info.append(detail.text)
    match_info_placeholder.header("Match Info")
    for info in match_info:
        match_info_placeholder.write(info)
    overs_info = []
    overs_details = soup1.select('.overs')
    for detail in overs_details:
        overs_info.append(detail.text)
    Overs_info_placeholder.header("Overs Info")
    for info in overs_info:
     if "This Over:" in info:
        if "4" in info and show_warning:
            st.warning("That's a FOUR!")
            show_warning = False
        elif "6" in info and show_warning:
            st.success("That's a SIX!")
            show_warning = False
        elif ("W" in info or "w" in info) and show_warning:
            st.warning("That's a WICKET!")
            show_warning = False
        else:
            show_warning = True
        Overs_info_placeholder.write(info) 
        
            
    Commentry_info = []
    Commentry_details = soup1.select('.d-flex')
    for detail in Commentry_details:
        Commentry_info.append(detail.text)
    Commentry_info_placeholder.header("Overs Info")
    for info in Commentry_info:
       Commentry_info_placeholder.write(info) 
    time.sleep(3)



