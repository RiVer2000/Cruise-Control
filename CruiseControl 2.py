import numpy as np
import matplotlib.pyplot as plt

m = 1200
v=0
Vel=[]
t=0
T_Fr = [30, 100, 250]
V_Fr = [70, 50, 100]
Time = [i for i in range(250)]
b = 50
kp = 52
ki = 8
kd = 0
j = 0
while(t != 250):
    r = V_Fr[j]
    old_e = 0
    E = 0
    while t!= T_Fr[j]:
        e = r-v
        e_dot = e - old_e
        E = E + e
        u = kp*e + kd*e_dot + ki*E
        old_e = e
        v = (m*v+u*t)/(m+b*t)
        Vel.append(v)
        t+=1
    j=j+1
print(Vel)
plt.plot(Time,Vel)
plt.xlabel('Time (sec)--->')
plt.ylabel('Velocity (m/s)--->')
plt.title("Cruise Control\n")
plt.show()