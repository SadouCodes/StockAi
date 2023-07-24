# Description: This file contains the code for the data visualization of the stock market data.

import pandas as pd
import yfinance as yf
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns

import data_extraction as de

def data_visualization(Stock = 'GOOG', StartDate = '2020-01-01', EndDate = '2023-06-01', Interval = '1mo'):
    data = de.extract_data(Stock, StartDate, EndDate, Interval)
    
    sns.set_theme()
    sns.relplot(data=data['Open'], kind='line', )
    sns.relplot(data=data['Close'], kind='line')

    plt.show()
    return

data_visualization('GOOG', '2020-01-01', '2023-06-01', '1mo')