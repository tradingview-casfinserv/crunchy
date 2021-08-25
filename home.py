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
    stock_data = stock.get_stock_data("TCS")
    # TCS
    st.title(stock_data["Meta Data"]["2. Symbol"])
    col1, col2, col3 = st.columns(3)

    keys_list = list(stock_data["Time Series (Daily)"])

    col1.metric(label=keys_list[0], value=stock_data["Time Series (Daily)"][keys_list[0]]["4. close"],
                                           delta=round((float(stock_data["Time Series (Daily)"][keys_list[0]]["4. close"]) -
                                                  float(stock_data["Time Series (Daily)"][keys_list[1]]["4. close"])), 2))
    col2.metric(label=keys_list[1], value=stock_data["Time Series (Daily)"][keys_list[1]]["4. close"],
                delta=round((float(stock_data["Time Series (Daily)"][keys_list[1]]["4. close"]) -
                             float(stock_data["Time Series (Daily)"][keys_list[2]]["4. close"])), 2))
    col3.metric(label=keys_list[2], value=stock_data["Time Series (Daily)"][keys_list[2]]["4. close"],
                delta=round((float(stock_data["Time Series (Daily)"][keys_list[2]]["4. close"]) -
                             float(stock_data["Time Series (Daily)"][keys_list[3]]["4. close"])), 2))

    stock_data = stock.get_stock_data("INFY")
    st.title(stock_data["Meta Data"]["2. Symbol"])
    col1, col2, col3 = st.columns(3)

    keys_list = list(stock_data["Time Series (Daily)"])

    col1.metric(label=keys_list[0], value=stock_data["Time Series (Daily)"][keys_list[0]]["4. close"],
                delta=round((float(stock_data["Time Series (Daily)"][keys_list[0]]["4. close"]) -
                             float(stock_data["Time Series (Daily)"][keys_list[1]]["4. close"])), 2))
    col2.metric(label=keys_list[1], value=stock_data["Time Series (Daily)"][keys_list[1]]["4. close"],
                delta=round((float(stock_data["Time Series (Daily)"][keys_list[1]]["4. close"]) -
                             float(stock_data["Time Series (Daily)"][keys_list[2]]["4. close"])), 2))
    col3.metric(label=keys_list[2], value=stock_data["Time Series (Daily)"][keys_list[2]]["4. close"],
                delta=round((float(stock_data["Time Series (Daily)"][keys_list[2]]["4. close"]) -
                             float(stock_data["Time Series (Daily)"][keys_list[3]]["4. close"])), 2))

    stock_data = stock.get_stock_data("RELIANCE")
    st.title(stock_data["Meta Data"]["2. Symbol"])
    col1, col2, col3 = st.columns(3)

    keys_list = list(stock_data["Time Series (Daily)"])

    col1.metric(label=keys_list[0], value=stock_data["Time Series (Daily)"][keys_list[0]]["4. close"],
                delta=round((float(stock_data["Time Series (Daily)"][keys_list[0]]["4. close"]) -
                             float(stock_data["Time Series (Daily)"][keys_list[1]]["4. close"])), 2))
    col2.metric(label=keys_list[1], value=stock_data["Time Series (Daily)"][keys_list[1]]["4. close"],
                delta=round((float(stock_data["Time Series (Daily)"][keys_list[1]]["4. close"]) -
                             float(stock_data["Time Series (Daily)"][keys_list[2]]["4. close"])), 2))
    col3.metric(label=keys_list[2], value=stock_data["Time Series (Daily)"][keys_list[2]]["4. close"],
                delta=round((float(stock_data["Time Series (Daily)"][keys_list[2]]["4. close"]) -
                             float(stock_data["Time Series (Daily)"][keys_list[3]]["4. close"])), 2))

