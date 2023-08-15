import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as optimization

NUM_TRADING_DAYS=252
NUM_PORTFOLIOS=10000
# stocks to be handled
stocks = ['AAPL','WMT','TSLA','GE','AMZN','DB']
start_date='2010-01-01'
end_date='2017-01-01'

def download_data():
    # create a dictionary w name -key and stock values-values
    stock_data = {}
    for stock in stocks:
        ticker=yf.Ticker(stock)
        stock_data[stock]=ticker.history(start=start_date,end=end_date)['Close']
    return pd.DataFrame(stock_data)

def show_data(data):
    data.plot(figsize=(10,5))
    plt.show()

def calculate_return(data):
    log_return=np.log(data/data.shift(1))
    return log_return[1:]

def show_statistics(returns):
    print(returns.mean()*NUM_TRADING_DAYS)
    print(returns.cov() * NUM_TRADING_DAYS)

def show_mean_variance(returns,weights):
    portfolio_returns=np.sum(returns.mean()*weights)*NUM_TRADING_DAYS
    portfolio_risk=np.sqrt(np.dot(weights.T,np.dot(returns.cov()*NUM_TRADING_DAYS,weights)))
    print("Expected portfolio return: ",portfolio_returns)
    print("Expected portfolio volatility: ",portfolio_risk)

def show_portfolios(returns,volatilities):
    plt.figure(figsize=(10,6))
    plt.scatter(volatilities,returns,c=returns/volatilities,marker='o')
    plt.grid(True)
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Return')
    plt.colorbar(label='Sharpe Ratio')
    plt.show()
def generate_portfolio(returns):
    portfolio_mean=[]
    portfolio_risks=[]
    portfolio_weights=[]

    for _ in range(NUM_PORTFOLIOS):
        w=np.random.random(len(stocks))
        w=w/np.sum(w)
        portfolio_weights.append(w)
        portfolio_mean.append((np.sum(returns.mean()*w))*NUM_TRADING_DAYS)
        portfolio_risks.append(np.sqrt(np.dot(w.T,np.dot(returns.cov()*NUM_TRADING_DAYS,w))))

    return np.array(portfolio_weights), np.array(portfolio_mean), np.array(portfolio_risks)

def statistics(weights, returns):
    portfolio_return = np.sum(returns.mean() * weights) * NUM_TRADING_DAYS
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * NUM_TRADING_DAYS, weights)))

    return np.array([portfolio_return, portfolio_volatility, portfolio_return/portfolio_volatility])

def min_function_sharpe(weights,returns):
    return -statistics(weights,returns)[2]

def optimize_portfolio(weights,returns):
    constraints={'type':'eq','fun':lambda x:np.sum(x)-1}
    bounds=tuple((0,1) for _ in range(len(stocks)))
    return optimization.minimize(fun=min_function_sharpe, x0=weights[0], args=returns, method='SLSQP', bounds=bounds, constraints=constraints)

def print_optimal_portfolio(optimum, returns):
    print("Optimal portfolio", optimum['x'].round(3))
    print("Expected return, volatility and Sharpe ratio", statistics(optimum['x'].round(3),returns))

def show_optimal_portfolios(opt,rets, portfolio_rets, portfolio_vols):
    plt.figure(figsize=(10,6))
    plt.scatter(portfolio_vols,portfolio_rets,c=portfolio_rets/portfolio_vols,marker='o')
    plt.grid(True)
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Return')
    plt.colorbar(label='Sharpe Ratio')
    plt.plot(statistics(opt['x'],rets)[1],statistics(opt['x'],rets)[0], 'g*', markersize=20)
    plt.show()

if __name__ == '__main__':
    print(download_data())
    data=download_data()
    show_data(data)
    returns_log=calculate_return(data)
    # show_statistics(returns_log)

    pweights,means,risks=generate_portfolio(returns_log)
    show_portfolios(means, risks)
    optimum=optimize_portfolio(pweights,returns_log)
    print_optimal_portfolio(optimum, returns_log)
    show_optimal_portfolios(optimum,returns_log,means,risks)
