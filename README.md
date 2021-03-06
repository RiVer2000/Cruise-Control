# Cruise-Control
# Aim  
To Develop a Cruise Control for a car for a Fixed point velocity using PID controller and then extended to Array of Velocities in Python.
# Motion Model  
The model of the cruise control system is relatively simple. If the inertia of the wheels is neglected,
and it is assumed that air drag (which is proportional to the car’s speed at low speeds) is what is
opposing the motion of the car, along with rolling friction and on a slope downwards gravity,
then the problem is reduced to a simple first order system.    

Broadly speaking considering only air drag, the motion of the car can be written as,  
                        *m.vdot + b.v = u*  
where m is mass of the car, b is air drag coefficient and u is the Input Force provided by the car to move the
car at the desired velocity.  
# Results  
1. The car was desired to hit 70kmph and stay at that velocity for a fixed point velocity system
[![solarized dualmode](https://github.com/RiVer2000/Cruise-Control/blob/master/Figure_1a.png)](#features)  
2. For an altered model the car was set to reach desired velocity which changed with respect to time
[![solarized dualmode](https://github.com/RiVer2000/Cruise-Control/blob/master/Figure_1b.png)](#features)  
#  Errors
Maximum errors that arose in the model were due to inappropriate values of the PID coefficients(Kp, Kd, Ki)    
1. If the value of Ki was taken too high then the system started oscillating which is undesireable  
[![solarized dualmode](https://github.com/RiVer2000/Cruise-Control/blob/master/Error1.png)](#features)  
2. Also we need sufficiently fast paced response thus Kd should be included as Kp alone cannot reach the 
goal velocity  
[![solarized dualmode](https://github.com/RiVer2000/Cruise-Control/blob/master/Error2.png)](#features)  
3. The Ki parameter was especially important in regard. The car didn't reach even near the desired velocity 
without the Integral gains.  
[![solarized dualmode](https://github.com/RiVer2000/Cruise-Control/blob/master/Error3.png)](#features)  
