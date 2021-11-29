import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

#stocks that you own
tickers = ['BTC-EUR', 'ETH-EUR', 'MANA-EUR', 'SAND-EUR', 'ENJ-EUR']
#Weught of the portfolio in percentages.
weights = np.array([0.58, 0.26, 0.082, 0.056, 0.022])

#calculates the returns of the portfolio and draws the plot.
def portFolioOfSecurities(beginningDay):
    data = pd.DataFrame()
    for ticker in tickers:
        data[ticker] = wb.DataReader(ticker, data_source='yahoo', start=beginningDay)['Close']
    #Normalization to 100. Comparing starts from the zero.
    (data / data.iloc[0] * 100).plot(figsize=(10, 5));
    plt.title("Portfolio stocks closing prices.")
    plt.show()

    returns = (data / data.shift(1)) - 1

    #Banks are open 250 days/year.
    annual_returns = returns.mean() * 250
    print(annual_returns)


    portfolio = str(round(np.dot(annual_returns, weights), 5) * 100) + ' %'
    print("Portfolio's annual returns: ")
    print(portfolio)


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
    print(stockName + "'s average annual return is: " + str(round(annual_return, 4) * 100) + '%')

#Calculate Log returns ln(Pt/Pt-1)
def stock_log_return(stockName, beginningDay, to):
    stock = wb.DataReader(stockName, data_source='yahoo', start=beginningDay, end=to)

    stock['log_return'] = np.log(stock['Adj Close'] / stock['Adj Close'].shift(1))

    stock['log_return'].plot(figsize=(10, 5))
    plt.title(stockName + "'s simple return")
    plt.show()

    daily_log_return = stock['log_return'].mean()
    print(stockName + "s avarage annual log return per day is: " + str(round(daily_log_return, 6) * 100) + '%')

    annual_log_return = stock['log_return'].mean() * 250
    print(stockName + "'s average log return is: " + str(round(annual_log_return, 4) * 100) + '%')


if __name__ == '__main__':
    # for stock in tickers:
    #     stockSimplereturn(stock, '2020-1-1', '2021-1-10')
    portFolioOfSecurities('2021-01-05')





