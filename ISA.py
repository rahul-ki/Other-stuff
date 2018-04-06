# input a height and it gives the temperature, pressure and density of air at that height.
# divide atmosphere based on Troposphere, Tropopause, StratosphereA etc. 

def Troposphere(h):
    a=-0.0065
    T=288.15+(a*h)
    P=101325*((T/288.15)**((-9.80065)/(287*a)))
    rho=P/(T*287)
    return P,T,rho

def Tropopause(h):
    P,T,rho=Troposphere(11000)
    P=P*math.exp((-9.80065)*(h-11000)/(287*T))
    rho=P/(287*T)
    return P,T,rho

def StratosphereA(h):
    P,T,rho=Tropopause(20000)
    a=0.001
    T2=T+(a*(h-20000))
    P=P*((T2/T)**((-9.80065)/(287*a)))
    rho=P/(287*T2)
    return P,T2,rho

def StratosphereB(h):
    P,T,rho=StratosphereA(32000)
    a=0.0028
    T3=T+(a*(h-32000))
    P=P*((T3/T)**((-9.80065)/(287*a)))
    rho=P/(287*T3)
    return P,T3,rho

def Stratopause(h):
    P,T,rho=StratosphereB(47000)
    P=P*math.exp((-9.80065)*(h-47000)/(287*T))
    rho=P/(287*T)
    return P,T,rho
    
    
import math
h=input ("Enter altitude in metres TILL 49KM  for finding corresponding P,T, rho:")

if h<=11000:
    e,f,g=Troposphere(h)
    print "Pressure: ", e, "Pa"
    print "Temp: ", f, "K"
    print "rho: ", g, "kg/ m cubed"

elif h<=20000:
    e,f,g=Tropopause(h)
    print "Pressure: ", e, "Pa"
    print "Temp: ", f, "K"
    print "rho: ", g, "kg/ m cubed"

elif h<=32000:
    e,f,g=StratosphereA(h)
    print "Pressure: ", e, "Pa"
    print "Temp: ", f, "K"
    print "rho: ", g, "kg/ m cubed"

elif h<=47000:
    e,f,g=StratosphereB(h)
    print "Pressure: ", e, "Pa"
    print "Temp: ", f, "K"
    print "rho: ", g, "kg/ m cubed"

elif h<=49000:
    e,f,g=Stratopause(h)
    print "Pressure: ", e, "Pa"
    print "Temp: ", f, "K"
    print "rho: ", g, "kg/ m cubed"

