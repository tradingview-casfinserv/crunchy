import streamlit as st
import requests, redis
import config, json
from iex import IEXStock
from helpers import format_number
from datetime import datetime, timedelta

symbol = st.sidebar.text_input("Symbol", value='MSFT')

screen = st.sidebar.selectbox("View", ('Overview', 'Fundamentals', 'News', 'Ownership', 'Technicals'), index=1)
stock = IEXStock(config.IEX_TOKEN, symbol)
st.title(screen)

if screen == 'Overview':
    url  = "https://api.twelvedata.com/symbol_search?symbol=tcs"
    r = requests.get(url)
    print(r.json())
    st.write(r.json())
