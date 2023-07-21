import tensorflow as tf
import yfinance as yf

print("TensorFlow Version: " + tf.__version__ + "\n")

data = yf.download(['GOOG', 'META', 'AMZN', 'TSLA'], interval="1d", start="2020-01-01", end="2023-06-01", group_by="ticker")
data1 = yf.download('GOOG', interval="1d", start="2020-01-01", end="2023-06-01", group_by="ticker")

#for ticker in data1:
#    print(ticker)

print(data1.head())

google = yf.Ticker("GOOG")


print(google.info)





