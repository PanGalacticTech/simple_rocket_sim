
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
    
    Mfr = mass flow rate of expended propellant kg/s
    
Equation:    
    Fthrust = g * Isp * Mfr
    
Input Variables:

    Mfr = 10 kg/s

'''



def thrust_isp_flow(Isp, Mfr):
    Fthrust = round(g*Isp*Mfr, 5)
    print("Thrust = ")
    print("[",Fthrust, "] N = [",g,"] m/s^(-2) x [",Isp,"] s x [",Mfr,"] kg/s ")
    return Fthrust

mass_flow_rate = 10   # kg/s
isp = 300  # s

thrust_isp_flow(isp, mass_flow_rate)



def burn_duration_from_mfr(Mfr, fuel_mass):
    burn_duration = fuel_mass / Mfr
    print("burn_duration = fuel_mass / Mfr")
    print("[", burn_duration, "] s = [", fuel_mass, "] kg / [", Mfr, "] kg/s ")
    return burn_duration

fuel_total_mass = 100    # kgs

burn_duration_from_mfr(mass_flow_rate, fuel_total_mass)

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
http://www.pro38.com/products/pro75/motor.php
    code	  Total Impulse (Ns)     Burn Duration (s)     Peak Thrust (ib)  prop type
8429M2020-P         8429                   4.2                603              Imax™


Vehicle Dry Mass: 
Vehicle Wet Mass:
Propellant Mass:
'''


def thrust_impulse_duration(impulse_total, burn_duration):
    thrust =  round(impulse_total / burn_duration, 5)
    print("Thrust = impulse_total / burn_duration")
    print("[",thrust, "] N = [", impulse_total , "] Ns / [", burn_duration, "] s")

impulse_total = 8429   # Ns
burn_duration = 4.2    # s



print("Micro Case Solid Rocket Motor")

thrust_impulse_duration(impulse_total,burn_duration)

