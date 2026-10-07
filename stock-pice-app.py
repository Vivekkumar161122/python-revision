import streamlit as st
import yfinance as yf

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google!
""")

# Define the ticker symbol
tickerSymbol = 'GOOGL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker (using start and end only)
tickerDf = tickerData.history(start='2010-05-31', end='2020-05-31')

# Display charts
st.subheader("Closing Price")
st.line_chart(tickerDf['Close'])

st.subheader("Volume")
st.line_chart(tickerDf['Volume'])
