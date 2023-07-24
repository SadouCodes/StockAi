import pandas as pd
import yfinance as yf
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns


def extract_data(Stock = 'GOOG', StartDate = '2020-01-01', EndDate = '2023-06-01', Interval = '1mo'):
    data = yf.download(Stock, interval=Interval, start=StartDate, end=EndDate)
    return data

def extract_data_2(Stock = 'GOOG', StartDate = '2020-01-01', EndDate = '2023-06-01', Interval = '1mo'):
    google = yf.Ticker(Stock)
    data = google.history(start=StartDate, end=EndDate, interval=Interval)
    return data


print(extract_data('GOOG', '2020-01-01', '2023-06-01', '1mo'))