import yfinance as yf

import datetime 

startDate = datetime.datetime(2020, 1, 1)
endDate = datetime.datetime(2023, 6, 1)

GetMetaInfo = yf.Ticker("META")

GetMetaInfo

print("Meta Info\n")
print(GetMetaInfo.info)
print("\n")

print("Meta History\n")
print(GetMetaInfo.history(start=startDate, end=endDate))

print("Meta News\n")
print(GetMetaInfo.news)

print("Meta Earnings\n")
print(GetMetaInfo.cashflow)