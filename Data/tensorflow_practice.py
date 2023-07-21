import tensorflow as tf
import yfinance as yf

print("TensorFlow Version: " + tf.__version__ + "\n")

data = yf.download(['GOOG', 'META', 'AMZN', 'TSLA'], start="2020-01-01", end="2023-06-01", group_by="ticker")

print(data.head())






