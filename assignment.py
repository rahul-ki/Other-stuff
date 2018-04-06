import math

ans="A"

    #ISA formula
#### i put this up so that i can use this throughout my program, and not just while f==1
g=9.80665
groundpressure=101325
R=287
T0=288.15
rho0=1.225

while ans!="Q":
    print "1. Entering height to find Pressure, Temperature and density."
    print "2. Finding Altitude from Pressure."
    print "3. Finding Altitude from Density."
    print "4. Quit."

    f=input("Enter the above options [1,2,3,4 or 5]:")

#Entering height to find Pressure, Temperature and density
    
    if f==1:
        s= input("Enter 1 if height is in feet. Enter 2 is height is in metres :- ") #I removed float() coz with float s becomes 1.0 or 2.0 Then you would have to change your "if s!=1.." to "if s!=1.0" 

        if s!=1 and s!=2:
            print "Your input is not 1 or 2. Restart program and try again."
            break   

        d= float(input("Enter the altitude in the units specified before :- "))

        if s==1:                  
            h=0.3048*d
        elif s == 2:                 
            h=d
            
        if h<=11000:                   #changed h<11000 to h<=11000 to include 11000
            a= -0.0065
            m=a*h
            T1 = (T0 + m)
            Pressure = groundpressure * (T1/T0)**(-g/(R*a))
            Rho = rho0 * (T1/T0)**((-g/(R*a))-1)
            rel_p= Pressure/groundpressure * 100
            rel_rho= Rho/rho0*100
            print "The temperature is", T1, "Kelvin, the pressure is", Pressure, "pascals and the density is", Rho, ".The pressure relative to sea level is", rel_p, "and the density relative to sea level is", rel_rho
            print ""
            
        elif 11000<h<=20000:                    
            h=h
            T2=288.15-(0.0065*11000)
            P1=groundpressure * (T2/T0)**(-g/(R*(-0.0065)))
            rho1= P1/(R*T2)
            Pressure = P1 * math.exp(-9.80665*(h-11000)/(R*T2))  #pressure at h=11km
            Rho = rho1 * math.exp(-9.80665*(h-11000)/(R*T2))   ## density at h=11km
            rel_p = Pressure / groundpressure * 100
            rel_rho = Rho / rho0 * 100
            print "The temperature is" , T2 , "Kelvin, the pressure is" ,Pressure, "pascals and the density is", Rho, ".The pressure relative to sea level is", rel_p, "and the density relative to sea level is", rel_rho
            print ""

#2.Finding Altitude from Pressure 

    elif f==2:      #making this till 20km 

        p=float(input("Enter pressure in Pa:"))
        if p>=22625.7914896:    #Pressure at h=11km
            a=-0.0065
            h=(T0/a)*(((p/groundpressure)**(-(a*R)/g))-1)
        elif p>=5471.93507195:  #Pressure at h=20km
            P1=groundpressure * (216.65/T0)**(-g/(R*(-0.0065)))
            h=11000+(((R*216.65)/g)*math.log((P1/p),math.exp))
        else:
            print "Sorry, height cant be determined."
        print h, "in metres"
        print ""


#3.Finding Altitude from Density

    elif f==3:    #making this till 20km
        den=float(input("Enter pressure in kg cubed:"))
        if den>=0.363817166677:
            a=-0.0065
            h=(T0/a)*((den/rho0)**((-1)/((g/(a*R))+1))-1)
        elif den>=0.0880035811699:
            P1=groundpressure * (216.65/T0)**(-g/(R*(-0.0065)))
            rho1=P1/(R*216.65)
            h=11000+(((R*216.65)/g)*math.log((rho1/den),math.exp))
        else:
            print "Sorry, height cant be determined."
        print h, "in metres"
        print ""

#4. Quit
    elif f==4:
        print "Program Aborting"
        ans="Q"
        
    else:
        print "Wrong input. Try again."

