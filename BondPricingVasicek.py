import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

NUM_OF_SIMULATIONS=1000
NUM=200

def monte_carlo(x,r0,kappa,theta,sigma,T=1):

    dt=T/float(NUM)
    result=[]

    for _ in range(NUM_OF_SIMULATIONS):
        rates=[r0]
        for _ in range(NUM):
            dr = kappa * (theta - rates[-1]) * dt + sigma * np.sqrt(dt) * np.random.normal(0, 1)
            rates.append(rates[-1] + dr)
        result.append(rates)

    simulation_data=pd.DataFrame(result)
    simulation_data=simulation_data.T

    integral=simulation_data.sum()*dt
    present_value=np.exp(-integral)
    bond_price=x*np.mean(present_value)
    print("Bond price: $%.2f" % bond_price)

if __name__=='__main__':
    monte_carlo(1000,0.1,0.3,0.1,0.03)