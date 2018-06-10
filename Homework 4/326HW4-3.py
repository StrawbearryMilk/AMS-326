import numpy as np
import matplotlib.pyplot as plt

h = .001
a = 1000
n = round(a/h)
v0 = 10

def wind(u):
    return 4 * v0 * u / a * (1 - u / a)

def rad(u, v):
    return np.sqrt(u ** 2 + v ** 2)

def dxdt(u, radius, vb):
    return vb * u / radius

def dydt(u, v, radius, vb):
    return wind(u) - vb * v / radius

def dydx(u, v,radius, vb):
    return radius / (u*vb) * wind(u) - v/u

x5 = np.empty(n)
x10 = np.empty(n)
x15 = np.empty(n)
y5 = np.empty(n)
y10 = np.empty(n)
y15 = np.empty(n)

x5[0] = x10[0] = x15[0] = a
y5[0] = y10[0] = y15[0] = 0
x5[-1] = x10[-1] = x15[-1] = 0
y5[-1] = y10[-1] = y15[-1] = 0

def rk2D(vb, x, y):
    for i in range(n-1):
        radius = rad(x[i],y[i])
        k1 = dxdt(x[i], radius, vb)
        l1 = dydt(x[i], y[i], radius, vb)

        k2 = dxdt(x[i] - .5 * h * k1, radius, vb)
        l2 = dydt(x[i] - .5 * h * k1, y[i] + .5 * h * l1, radius, vb)

        k3 = dxdt(x[i] - .5 * h * k2, radius, vb)
        l3 = dydt(x[i] - .5 * h * k2, y[i] + .5 * h * l2, radius, vb)

        k4 = dxdt(x[i] - h * k3, radius, vb)
        l4 = dydt(x[i] - h * k3, y[i] + h * l3, radius, vb)

        k = 1 / 6 * (k1 + 2 * (k2 + k3) + k4)
        l = 1 / 6 * (l1 + 2 * (l2 + l3) + l4)

        x[i + 1] = x[i] - h * k
        y[i + 1] = y[i] + h * l



    return x, y

t1 = rk2D(5, x5, y5)
t2 = rk2D(10, x10, y10)
t3 = rk2D(15, x15, y15)

print(np.max(t1[1]))
print(np.max(t2[1]))
print(np.max(t3[1]))

def trajectoryPlot():
    plt.plot(t1[0], t1[1], color = "red", label = r"$v_B = 5$")
    plt.plot(t2[0], t2[1], color = "black", label = r"$v_B = 10$")
    plt.plot(t3[0], t3[1], color = "cyan", label = r"$v_B = 15$")
    plt.ylabel(r"$y(x)$")
    plt.xlabel(r"$x(t)$")
    plt.title("Boat Trajectory")

    plt.legend()
    plt.show()

trajectoryPlot()