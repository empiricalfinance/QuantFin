import numpy as np

def PriceFXForward(S0, Rdc,Rfc,T):
    # Pricing FX forward
    F=S0*(((1+Rdc)/(1+Rfc))**(T/365))
    return F

def ValueFXForward(St, F, Rdc,Rfc,T,t ):
    # valuation of Vt(F0:T)
    Val=St/((1+Rfc)**((T-t)/365))-F/((1+Rdc)**((T-t)/365))
    return Val

def CoveredIntArbitrage(S0,Fmkt,Rdc,Rfc,T):
# input: S0, spot rate
#           Fmkt, FX forward market price
#           Rdc, Domestic interest rate
#           Rfc, Foreign interest rate
#           T, the maturity of FX forward
#output: prof, profit investor earned
#            initial_currency: Initially, the currency investor should
#            lend from bank
    F=PriceFXForward(S0, Rdc,Rfc,T);
    if (F<Fmkt):
        prof =1000*((Fmkt/S0)*(1+Rfc)**(T/365)-(1+Rdc)**(T/365))
        initial_currency='DC'
    else:
        prof =1000*((S0/Fmkt)*(1+Rdc)**(T/365)-(1+Rfc)**(T/365))
        initial_currency='FC'

    return prof, initial_currency


#main function
Rdc=1/100
Rfc=3/100
T=365
S0=1.0625
#Pricing FX forward

F= PriceFXForward(S0, Rdc,Rfc,T)
#After 180 days, valuing Vt(F0:T)
t=180
St=1.1
Val= ValueFXForward(St, F, Rdc,Rfc,T,t)
print('What is the price of FX forward = ',F)
print("What is the Value of FX forward after %d = " %(t),Val)


Rdc=1/100;
Rfc=3/100;
T=365;
S0=1.0625;
Fmkt=1.0800;

prof,initial_currency=CoveredIntArbitrage(S0,Fmkt,Rdc,Rfc,T)

print('We earn profit=',prof,initial_currency)
