import streamlit as st
import requests
import config, json
from twelve_data_connector import *
from helpers import format_number
from datetime import datetime, timedelta
import pandas as pd

# symbol = st.sidebar.text_input("Symbol", value='MSFT')

stock = IEXStock(config.IEX_TOKEN)

if st.sidebar.button("Index"):
    st.title("casfinserv ❤️Index")
    index_list = stock.get_indexes()["data"]
    symbol_list = []
    name_list = []
    country_list = []
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
if st.sidebar.button("Stocks"):
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    col2.metric(label="Temperature", value="70 °F", delta="-1.2 °F")
    col3.metric(label="Temperature", value="70 °F", delta="1.2 °F")

