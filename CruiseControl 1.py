'''
This project was done by Rishabh Verma as an internsip project
under IvLabs

This project aims to achieve cruise control of a car in 1D 
using a PID controller wherin the case is of a vehicle on a 
slope
'''


#import all necessary Libraries

import numpy as np
import matplotlib.pyplot as plt
import math

'''
The system is modelled using
F = m*a
v = v(in) + a*t
a = (u - m*g*sin(theta)-b*v)/m
'''
m = 1200							#Mass of the Vehicle
v=0									#Current Velocity of the Vehicle
Vel=[]								#Velocity Array to store values at different times
t=0									#Current Time frame
Time = [i for i in range(50)]  		#Time array to plot graph
b = 50								#Constant for air drag
r = 70								#Reference Velocity
mu = 0.01							#Coefficient of Rolling friction
g=9.81								#Gravity
ms = 0.3							#Value of Slope
sin = ms/(math.sqrt(1 + ms**2))		#Value of Sine of Inclination
kp = 50								#Proportional gain constant
ki = 7.5								#Integral gain constant
kd = 19								#Differential gain constant


#Predefining the Error terms

old_e = 0	
E = 0

#Formulating the actual Cruise Control

while t!= 50:
	e = r-v
	e_dot = e - old_e
	E = E + e
	u = kp*e + kd*e_dot + ki*E
	old_e = e
	v = (m*v+ u*t + mu*m*t*g - m*g*sin)/(m+b*t)
	Vel.append(v)
	t+=1
print(Vel)							#Printing the velocities so as to get a better idea of them

#Plot the results obtained 

plt.plot(Time,Vel)
plt.xlabel('Time (sec)--->')
plt.ylabel('Velocity --->')
plt.title("Cruise Control\n")
plt.show()
