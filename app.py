import streamlit as st
import yfinance as yf
import pandas as pd
import ta

st.title("Indian Stock Analyzer 🇮🇳")

stock_name = st.text_input("Enter Stock Name (Example: RELIANCE.NS)")

if stock_name:
    data = yf.download(stock_name, period="6mo", interval="1d")

    if not data.empty:
        st.write("Latest Data")
        st.dataframe(data.tail())

        # Moving Averages
        data['SMA20'] = ta.trend.sma_indicator(data['Close'], window=20)
        data['SMA50'] = ta.trend.sma_indicator(data['Close'], window=50)

        latest_close = data['Close'].iloc[-1]
        sma20 = data['SMA20'].iloc[-1]
        sma50 = data['SMA50'].iloc[-1]

        st.write("### Technical Analysis")

        if latest_close > sma20 and sma20 > sma50:
            st.success("BUY Signal ✅")
        elif latest_close < sma20 and sma20 < sma50:
            st.error("SELL Signal ❌")
        else:
            st.warning("HOLD ⚠️")

        st.line_chart(data[['Close', 'SMA20', 'SMA50']])

    else:
        st.error("Invalid Stock Name")
