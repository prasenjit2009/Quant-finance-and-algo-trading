class CouponBond:
    def __init__(self,principal,rate,interest,maturity):
        self.principal=principal
        self.rate=rate/100
        self.interest=interest/100
        self.maturity=maturity

    def present_value(self,x,n):
        return x/(1+self.interest)**n

    def calculate_price(self):

        price=0

        # coupon payments
        for t in range(1,self.maturity+1):
            price=price+self.present_value(self.principal*self.rate,t)

        # principal amount
        price=price+self.present_value(self.principal,self.maturity)

        return price

if __name__ == '__main__':
    bond=CouponBond(1000,10,4,3)
    print("Bond price: %.2f" % bond.calculate_price())
