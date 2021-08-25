import streamlit as st
import requests, redis
import config, json
from twelve_data_connector import *
from helpers import format_number
from datetime import datetime, timedelta
import pandas as pd

# symbol = st.sidebar.text_input("Symbol", value='MSFT')

screen = st.sidebar.selectbox("View", ('Index', 'Fundamentals', 'News', 'Ownership', 'Technicals'), index=0)
# stock = IEXStock(config.IEX_TOKEN, symbol)
stock = IEXStock(config.IEX_TOKEN)
st.title(screen)

if screen == 'Index':
    index_list = stock.get_indexes()["data"]
    symbol_list = []
    name_list = []
    country_list = []
    # print(index_list)
    for index in index_list:
        symbol_list.append(index['symbol'])
        name_list.append(index['name'])
        country_list.append(index['country'])
    df = pd.DataFrame({
        'Symbol': symbol_list,
        'Name': name_list,
        'Country': country_list
    })

    st.table(df)


