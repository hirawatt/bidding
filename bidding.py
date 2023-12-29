import streamlit as st
import pandas as pd
import redis

# streamlit
st.set_page_config(
    'Bidding Portal',
    '🛎',
    layout='centered',
    initial_sidebar_state='collapsed',
    menu_items={
        "Get Help": "https://biddings.streamlit.app",
        "About": "Bidding Portal",
    },
)

r = redis.Redis(
    host=st.secrets['redis']['host'],
    port=st.secrets['redis']['port'],
    password=st.secrets['redis']['password'])

st.markdown("<h1 style='text-align: center; color: blue;'>Bidding Portal</h1>", unsafe_allow_html=True)

# Main Bidding Logic
def bid(team_name):
    amount = st.number_input("Bid Amount", value=100, step=100, min_value=100, label_visibility="collapsed")
    bid_success = st.button("Bid", use_container_width=True, type="primary")
    bid_info = {team_name: amount}
    
    # FIXME: create this function connecting to redis server
    #send_message(bid_info)

    # FIXME: add button logic
    co1, co2 = st.columns(2)
    #co1.button("Exit bid", use_container_width=True)
    co2.button("Refresh", use_container_width=True)

    if bid_success:
        st.write(bid_info)
        st.toast(f'Bid for {amount} was successfull!', icon='✅')
    else:
        st.info("Press Bid button to enter")
        #st.toast(f'Bid for {amount} unsuccessfull!', icon='❌')

# Login Check Screen
login_code = st.text_input("Enter code:")
if login_code:
    try:
        # add 3 digit login code to enter
        r_creds_folder = "auction:jpls5:creds:"
        r_creds_key = r_creds_folder + login_code
        r_creds_value = r.get(r_creds_key)
        team_name = r_creds_value.decode('utf-8')
        st.subheader(f"Welcome {team_name},")
        bid(team_name)
    except:
        st.warning("Incorrect Code. Try again")