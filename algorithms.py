
'''
This File Contains:
 - Raw maths algorithms for computing outputs
 - Macros defined to speed up typing
 - Useful algorithms for controlling program execution

'''

import math



# Global Variables

g = 9.80665  # ms^(-2)


'''
 The Rocket Equation
 
 Variables:
     dV = deltaV max change of velocity of the vehicle
     Mw = Mass (wet) of vehicle & Propellant
     Md = Mass (dry) of vehicle (no Propellant)
     Ve = effective exhaust velocity = Isp(g)
     Isp = Specific Impulse in dimension of time
     g = standard gravity
     ln = standard logarithm function
   
  Equation:   
     dV = Ve * ln(Mw/Md) = Isp * g * ln(Mw/Md)
     
     
    Input Constants
     g = 9.80665 ms^(-2)
     
    Input Variables
    Ve =  g * x m/s
    Isp =  x s (by weight)  or x  N s/kg  (by mass)
    
    Mw = 100 kg
    Md = 20 kg
     

'''

#ln = math.logg = 9.81


'''

Thrust

Variables:
    
    Mfr = mass flow rate of expended propellant 
    
Equation:    
    Fthrust = g * Isp * Mfr
    
Input Variables:

    Mfr = 10 kg/s

'''


def thrust_calc(Isp, Mfr):
    Fthrust = g*Isp*Mfr
    print("[",Fthrust, "] N = [",g," m/s^(-2) x [",Isp,"] s x [",Mfr,"] kg/s ")
    return Fthrust


thrust_calc(300, )


'''

Isp

Variables:

    Isp = specific impulse in seconds
    Ve = average exhast speed along the axis of the engine 

Equation:    
   Isp = Ve / g          (vac)

Input Variables:

    Isp = X s
    Ve = x m/s
    

'''


'''
Micro Case Solid Rocket Motor

    code	  Total Impulse (Ns)     Burn Duration (s)     Peak Thrust (ib)  prop type
8429M2020-P         8429                   4.2                603              Imax™


'''