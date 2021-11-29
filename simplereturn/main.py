import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


tickers = ['ENJ-EUR', 'BTC-EUR', 'ETH-EUR', 'MANA-EUR']

def portFolioOfSecurities(beginningDay):
    data = pd.DataFrame()
    for ticker in tickers:
        data[ticker] = wb.DataReader(ticker, data_source='yahoo', start=beginningDay)['Close']
    print(data.info())
    print(data.head())
    print(data.tail())

def stockSimplereturn(stockName, beginningDay, to):

    stock = wb.DataReader(stockName, data_source='yahoo', start= beginningDay, end=to)
    #adjusted close Pt/Pt-1
    stock['simple_return'] = (stock['Adj Close'] / stock['Adj Close'].shift(1)) - 1
    #OPrints the plot, size 10x5.
    stock['simple_return'].plot(figsize=(10,5))
    plt.title(stockName + "'s simple return")
    plt.show()
    #Average return per day.
    dailyReturn = stock['simple_return'].mean()
    print(stockName + "s avarage returns per day is: " + str(round(dailyReturn, 6) * 100) + '%')

    annual_return = stock['simple_return'].mean() * 250
    print(stockName + "'s average return is: " + str(round(annual_return, 4) * 100) + '%')

#Calculate Log returns ln(Pt/Pt-1)
def stock_log_return(stockName, beginningDay, to):
    stock = wb.DataReader(stockName, data_source='yahoo', start=beginningDay, end=to)

    stock['log_return'] = np.log(stock['Adj Close'] / stock['Adj Close'].shift(1))

    stock['log_return'].plot(figsize=(10, 5))
    plt.title(stockName + "'s simple return")
    plt.show()

    daily_log_return = stock['log_return'].mean()
    print(stockName + "s avarage log return per day is: " + str(round(daily_log_return, 6) * 100) + '%')

    annual_log_return = stock['log_return'].mean() * 250
    print(stockName + "'s average log return is: " + str(round(annual_log_return, 4) * 100) + '%')


if __name__ == '__main__':
    for stock in tickers:
        stockSimplereturn(stock, '2020-1-1', '2021-1-10')
    #portFolioOfSecurities('2020-1-1')





