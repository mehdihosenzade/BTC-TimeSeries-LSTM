import yfinance as yf
import pandas as pd

# دانلود قیمت بیت‌کوین
data = yf.download('BTC-USD', start='2019-01-01', end='2024-12-31')
print(data.head())
data.to_csv('btc_data.csv')
