
import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import datetime
import pandas_ta as pta  # Replacing 'ta' with pandas_ta
from pages.utils.plotly_fig import pplotly_table,candlestick,RSI,MACD,moving_average,close_chart

# Page config
st.set_page_config(
    page_title="Stock Analysis",
    page_icon=":page_with_curl:",
    layout="wide"
)

st.title("Stock Analysis")

# Columns for input
col1, col2, col3 = st.columns(3)
today = datetime.date.today()

with col1:
    ticker_symbol = st.text_input("Stock Ticker", "AAPL")
with col2:
    start_date = st.date_input("Choose Start Date",datetime.date(today.year - 1, today.month, today.day))
with col3: 
    end_date = st.date_input("Choose End Date",today)

# Stock profile
name = ''
if ticker_symbol == 'AAPL':
    name = 'APPLE'
elif ticker_symbol == 'MSFT':
    name = 'MICROSOFT'
else:
    name = ticker_symbol
st.subheader(f"{name} Profile")
stock = yf.Ticker(ticker_symbol)
info = stock.info

st.write(info.get("longBusinessSummary", "Not available"))
st.write("**Sector :**", info.get("sector", "Not available"))
st.write("**Employees :**", info.get("fullTimeEmployees", "Not available"))
st.write("**Website :**", info.get("website", "Not available"))

# Stock metrics
col1,col2 = st.columns(2)
with col1:
    df_metrics = pd.DataFrame({
        "Metric": ['Market Cap', 'Beta', 'EPS', 'PE Ratio',"Quick Ratio","Profit Margin","Revenue per Share","Debt to Equity","Return on Equity"],
        "Value": [
            info.get("marketCap", "N/A"),
            info.get("beta", "N/A"),
            info.get("trailingEps", "N/A"),
            info.get("trailingPE", "N/A"),
            info.get("quickRatio", "N/A"),
            info.get("profitMargins", "N/A"),
            info.get("revenuePerShare", "N/A"),
            info.get("debtToEquity", "N/A"),
            info.get("returnOnEquity", "N/A")
        ]
    })
    st.subheader("Financial Metric Table")
    fig1 = pplotly_table(df_metrics)
    st.plotly_chart(fig1)
    
    data = yf.download(ticker_symbol, start=start_date, end=end_date)
    
    if not data.empty and len(data) > 1:
        daily_change = float(data["Close"].iloc[-1] - data["Close"].iloc[-2])
        st.metric(
            label="Daily Change",
            value=round(float(data["Close"].iloc[-1]), 2),
            delta=round(daily_change, 2)
        )


with col2:
    hist = stock.history(start=start_date, end=end_date)

    if not hist.empty:
        st.subheader("Historical Data of Last 10 days")
        st.dataframe(hist.tail(10))

    else:
        st.write("No historical data found for this period.")

c1,c2,c3,c4,c5,c6,c7 = st.columns([1,1,1,1,1,1,1])
num_period = ''

with c1:
    if(st.button('5D')):
        num_period = '5d'

with c2:
    if(st.button('1M')):
        num_period = '1mo'

with c3:
    if(st.button('6M')):
        num_period = '6mo'

with c4:
    if(st.button('YTD')):
        num_period = 'ytd'

with c5:
    if(st.button('1Y')):
        num_period = '1y'


with c6:
    if(st.button('5Y')):
        num_period = '5y'

with c7:
    if(st.button('MAX')):
        num_period = 'max'

col1,col2,col3 = st.columns([1,1,4])

with col1:
    chart_type = st.selectbox('',('candle','line'))

with col2:
    if chart_type =='candle':
        indicators = st.selectbox('',('RSI','MACD'))
    else:
        indicators = st.selectbox('',('RSI','Moving Average','MACD'))

new1 = stock.history(period='max')
new2 = stock.history(period='max')

if num_period=='':
    if chart_type=='candle' and indicators=='RSI':
        st.plotly_chart(candlestick(new2,'1y'),use_container_width=True)
        st.plotly_chart(RSI(new2,'1y'),use_container_width=True)

    if chart_type=='candle' and indicators=='MACD':
        st.plotly_chart(candlestick(new2,'1y'),use_container_width=True)
        st.plotly_chart(MACD(new2,'1y'),use_container_width=True)

    if chart_type=='line' and indicators=='RSI':
        st.plotly_chart(close_chart(new2,'1y'),use_container_width=True)
        st.plotly_chart(RSI(new2,'1y'),use_container_width=True)

    if chart_type=='line' and indicators=='MACD':
        st.plotly_chart(close_chart(new2,'1y'),use_container_width=True)
        st.plotly_chart(MACD(new2,'1y'),use_container_width=True)

    if chart_type=='line' and indicators=='Moving Average':
        # st.plotly_chart(close_chart(new2,'1y'),use_container_width=True)
        st.plotly_chart(moving_average(new2,'1y'),use_container_width=True)

else:

    if chart_type=='candle' and indicators=='RSI':
        st.plotly_chart(candlestick(new2,num_period),use_container_width=True)
        st.plotly_chart(RSI(new2,num_period),use_container_width=True)

    if chart_type=='candle' and indicators=='MACD':
        st.plotly_chart(candlestick(new2,num_period),use_container_width=True)
        st.plotly_chart(MACD(new2,num_period),use_container_width=True)

    if chart_type=='line' and indicators=='RSI':
        st.plotly_chart(close_chart(new2,num_period),use_container_width=True)
        st.plotly_chart(RSI(new2,num_period),use_container_width=True)

    if chart_type=='line' and indicators=='MACD':
        st.plotly_chart(close_chart(new2,num_period),use_container_width=True)
        st.plotly_chart(MACD(new2,num_period),use_container_width=True)

    if chart_type=='line' and indicators=='Moving Average':
        # st.plotly_chart(close_chart(new2,num_period),use_container_width=True)
        st.plotly_chart(moving_average(new2,num_period),use_container_width=True)