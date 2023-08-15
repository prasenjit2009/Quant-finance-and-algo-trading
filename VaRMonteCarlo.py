import numpy as np
import yfinance as yf
import datetime
import pandas as pd

def download_data(stock,start,end):
    data={}
    ticker=yf.download(stock,start,end)
    data[stock]=ticker['Adj Close']
    return pd.DataFrame(data)

class ValueAtRiskMonteCarlo:
    def __init__(self,S,c,mu,sigma,n,iterations):
        self.S=S
        self.c=c
        self.mu=mu
        self.sigma=sigma
        self.n=n
        self.iterations=iterations

    def simulation(self):
        rand=np.random.normal(0,1,[1,self.iterations])
        stock_price=self.S*np.exp(self.n*(self.mu-0.5*self.sigma**2)+(self.sigma*np.sqrt(self.n)*rand))
        stock_price=np.sort(stock_price)
        percentile=np.percentile(stock_price,(1-self.c)*100)
        return self.S-percentile



if __name__=='__main__':
    S=1e6
    c=0.95
    n=1
    iterations=100000
    start_date=datetime.datetime(2014,1,1)
    end_date=datetime.datetime(2017,10,15)
    citi=download_data('C',start_date,end_date)
    citi['returns']=citi['Adj Close'].pct_change()
    mu=np.mean(citi['returns'])
    sigma=np.std(citi['returns'])
    model=ValueAtRiskMonteCarlo(S,c,mu,sigma,n,iterations)
    model.simulation()
    print('Value at risk with Monte Carlo simulation is: $%0.2f' % model.simulation())