import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


stockName = ['ENJ-EUR', 'BTC-EUR', 'ETH-EUR', 'MANA-EUR']

def stockSimplereturn(stockName, beginningDay, to):

    stock = wb.DataReader(stockName, data_source='yahoo', start= beginningDay, end=to)
    #adjusted close Pt/Pt-1
    stock['simple_return'] = (stock['Adj Close'] / stock['Adj Close'].shift(1)) - 1
    #OPrints the plot, size 10x5.
    stock['simple_return'].plot(figsize=(10,5))
    plt.show()
    #Average return per day.
    avg_returns_day = stock['simple_return'].mean()
    print(stockName + "s avarage returns per day is: " + str(round(avg_returns_day, 6) * 100) + '%')

    avg_returns_a = stock['simple_return'].mean() * 250
    print(stockName + "'s average return is: " + str(round(avg_returns_a, 4) * 100) + '%')

#Calculate Log returns ln(Pt/Pt-1)
def stock_log_return(stockName, beginningDay, to):
    stock = wb.DataReader(stockName, data_source='yahoo', start=beginningDay, end=to)

    stock['log_return'] = np.log(stock['Adj Close'] / stock['Adj Close'].shift(1))

    stock['log_return'].plot(figsize=(10, 5))
    plt.text(0.5,5, stockName + " log returns.")
    plt.show()

    log_returns_day = stock['log_return'].mean()
    print(stockName + "s avarage log return per day is: " + str(round(log_returns_day, 6) * 100) + '%')

    log_returns_a = stock['log_return'].mean() * 250
    print(stockName + "'s average log return is: " + str(round(log_returns_a, 4) * 100) + '%')


if __name__ == '__main__':
    for stock in stockName:
        stockSimplereturn(stock, '2020-1-1', '2021-1-10')



