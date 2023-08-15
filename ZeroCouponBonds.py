class ZeroCouponBonds:

    def __init__(self,principal,interest,maturity):
        self.principal=principal
        self.interest=interest/100
        self.maturity=maturity

    def present_value(self,x,n):
        return x/(1+self.interest)**n

    def calculate_price(self):
        return self.present_value(self.principal,self.interest)

if __name__== '__main__':
    bond=ZeroCouponBonds(1000,4,2)
    print("Price of the bond is: %s" % bond.calculate_price())