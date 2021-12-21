
import pandas as pd
import yfinance as yf
from pytrends.request import TrendReq
from matplotlib import pyplot as plt

pytrend = TrendReq()
symbol = 'tsla'
kw_list = [f'buy {symbol}', f'sell {symbol}']
pytrend.build_payload(kw_list, timeframe = 'now 1-H')
data = pytrend.interest_over_time()
prices = yf.download(symbol, period="1h", interval="1m")

print(data.iloc[-1], prices.iloc[-1])

plt.subplot(3,1,1)
plt.scatter(list(range(len(data[kw_list[0]]))), data[kw_list[0]])
plt.title(f'Relative frequency for {kw_list[0]}')

plt.subplot(3,1,2)
plt.scatter(list(range(len(prices['Open']))), prices['Open'])
plt.scatter(list(range(len(prices['Close']))), prices['Close'])
plt.legend(['Open','Close'])
plt.title(f'Close/open prices for {symbol}')

plt.subplot(3,1,3)
plt.scatter(list(range(len(data[kw_list[1]]))), data[kw_list[1]])
plt.title(f'Relative frequency for {kw_list[1]}')

plt.tight_layout()
plt.show()
