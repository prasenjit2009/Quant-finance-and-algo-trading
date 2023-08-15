from math import exp

def future_discrete(x,r,n):
    return x*(1+r)**(n)

def present_discrete(x,r,n):
    return x*(1+r)**(-n)

def future_continous(x,r,n):
    return x*exp(r*n)

def present_continous(x,r,n):
    return x*exp(r*n)

if __name__=='__main__':

    x=100
    r=0.05
    n=5

    print("Future value (discrete) of x: %s" % future_discrete(x,r,n))
    print("Present value (discrete) of x: %s" % present_discrete(x, r, n))
    print("Future value (continous) of x: %s" % future_continous(x, r, n))
    print("Present value (continous) of x: %s" % present_continous(x, r, n))

