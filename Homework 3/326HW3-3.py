#Jeffrey Rodriguez 110733867
import numpy as np
import matplotlib.pyplot as plt

a = 0.222
b = -0.0011
c = -1.999
e = 0.010
dt = 0.0001

n = int(round(11/dt))
x = np.empty(n)
y = np.empty(n)
t = np.empty(n)

t[0] = 0
x[0] = 199
y[0] = 21

def dxdt(t, u, v):
    return a * u + b * u * v


def dydt(t, u, v):
    return c * v + e * u * v

def rk2D():
    inst = np.zeros(3)  # used to store first instance of y > x
    for i in range(n-1):
        k1 = dxdt(t[i], x[i], y[i])
        l1 = dydt(t[i], x[i], y[i])

        k2 = dxdt(t[i] + .5 * dt, x[i] + .5 * dt * k1, y[i] + .5 * dt * l1)
        l2 = dydt(t[i] + .5 * dt, x[i] + .5 * dt * k1, y[i] + .5 * dt * l1)

        k3 = dxdt(t[i] + .5 * dt, x[i] + .5 * dt * k2, y[i] + .5 * dt * l2)
        l3 = dydt(t[i] + .5 * dt, x[i] + .5 * dt * k2, y[i] + .5 * dt * l2)

        k4 = dxdt(t[i] + dt, x[i] + dt * k3, y[i] + dt * l3)
        l4 = dydt(t[i] + dt, x[i] + dt * k3, y[i] + dt * l3)

        k = 1 / 6 * (k1 + 2 * (k2 + k3) + k4)
        l = 1 / 6 * (l1 + 2 * (l2 + l3) + l4)

        if (np.all(inst == 0)):
            if (y[i] > x[i]):
                inst = [t[i], y[i], x[i]]

        t[i + 1] = t[i] + dt
        x[i + 1] = x[i] + dt * k
        y[i + 1] = y[i] + dt * l



    return t, x, y, inst

t, x, y, inst = rk2D()

##1
print(x[-1])
print(y[-1])

def phasePlot():
    plt.plot(x,y,label= "Phase Diagram for Stocks")
    plt.ylabel(r"$y(t)$")
    plt.xlabel(r"$x(t)$")
    plt.title("Stock Value Phase Diagram for $t\in[0,11]$")

    plt.show()
phasePlot()

##3
print(inst)
