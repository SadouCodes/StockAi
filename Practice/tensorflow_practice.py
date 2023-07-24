import tensorflow as tf
import yfinance as yf

print("TensorFlow Version: " + tf.__version__ + "\n")

data = yf.download(['GOOG', 'META', 'AMZN', 'TSLA'], interval="1d", start="2020-01-01", end="2023-06-01", group_by="ticker")

#for ticker in data1:
#    print(ticker)

tf.print(data.head())

mode = tf.keras.Sequential([
])

v = tf.Variable([2,3], dtype=tf.float32)

tf.print(v)

x = tf.constant(10.0, name ='x', dtype=tf.float32)
y = tf.constant(10, name ='y', dtype=tf.int64)
z = tf.constant(30, name ='z', dtype=tf.float32)

print(x)






