# Cruise-Control
# Aim  
To Develop a Cruise Control for a car for a Fixed point velocity and then extened to Array of Velocities in Python.
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
