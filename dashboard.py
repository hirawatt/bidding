import streamlit as st
import pandas as pd

# credentials
page_title = "CricStars - Dashboard"

# streamlit
st.set_page_config(
    '{}'.format(page_title),
    '🏏',
    layout='wide',
    initial_sidebar_state='collapsed',
    menu_items={
        "Get Help": "https://cricstars.streamlit.app",
        "About": "CrickStars App",
    },
)

players_list_upload = st.sidebar.file_uploader("Upload Players List", type=["csv"])
if players_list_upload is not None:
    players_list = pd.read_csv(players_list_upload)
    st.dataframe(players_list)
else:
    st.info("Upload players list to continue")

