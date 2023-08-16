import streamlit as st
import pandas as pd

players_list_upload = st.file_uploader("Upload Players List", type=["csv"])
players_list = pd.read_csv(players_list_upload)
st.dataframe(players_list)

