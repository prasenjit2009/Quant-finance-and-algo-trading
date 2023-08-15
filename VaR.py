import numpy as np
import yfinance as yf
import pandas as pd
import datetime
from scipy.stats import norm

def download_data(stock,start_date,end_date):
    data={}
    ticker=yf.download(stock,start_date,end_date)
    data[stock]=ticker['Adj Close']
    return pd.DataFrame(data)

def calculate_var(S,c,mu,sigma):
    var=S*(mu-sigma*norm.ppf(1-c))
    return var

def calculate_var_t(S,c,mu,sigma,t):
    var=S*(mu*t-sigma*np.sqrt(t)*norm.ppf(1-c))
    return var



if __name__=='__main__':
    start=datetime.datetime(2014,1,1)
    end=datetime.datetime(2018,1,1)

    stock_data=download_data('C',start,end)
    stock_data['returns']=np.log(stock_data['C']/stock_data['C'].shift(1))
    stock_data=stock_data[1:]
    print(stock_data)
    mu=np.mean(stock_data['returns'])
    sigma=np.std(stock_data['returns'])
    S=1e6
    c=0.95
    t=10
    print('Value at risk for tomorrow is : %0.2f' % calculate_var(S,c,mu,sigma))
    print('Value at risk for 10 days is : %0.2f' % calculate_var_t(S,c,mu,sigma,t))

