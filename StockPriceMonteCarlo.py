import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

NUM_OF_SIMULATIONS=100

def stock_monte_carlo(S0, mu, sigma, N=1000):
    result=[]

    for _ in range(NUM_OF_SIMULATIONS):
        prices=[S0]
        for _ in range(N):
            stock_price=prices[-1]*np.exp((mu-0.5*sigma**2)+sigma*np.random.normal())
            prices.append(stock_price)

        result.append(prices)

    simulation_data=pd.DataFrame(result)
    simulation_data=simulation_data.T
    simulation_data['mean']=simulation_data.mean(axis=1)

    plt.plot(simulation_data['mean'])
    plt.show()

    print(simulation_data)


if __name__=='__main__':
    stock_monte_carlo(50,0.0002,0.01)

