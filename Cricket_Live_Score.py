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
st.title("Live Score Update Faster then your expectations")
st.header('Watch Online Streaming')
iframe_html = <iframe src="//stream.crichd.vip/update/skys2.php" width="100%" height="400px" frameborder="0" allowfullscreen></iframe>
st.markdown(iframe_html, unsafe_allow_html=True)
st.title("Match Updates")
match_info_placeholder = st.empty()

link = 'https://www.cricketworld.com/cricket/gujarat-titans-vs-mumbai-indians/match/live/62446'

while True:
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



