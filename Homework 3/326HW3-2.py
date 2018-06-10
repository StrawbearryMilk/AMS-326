#Jeffrey Rodriguez 110733867
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

A = 33.33
T0 = 98.88
Ta = 91.11
T120 = 66.66
Tb = 44.44
n = 1000000
t = np.empty(n)
T = np.empty(n)
t[0] = 0
h = .001

def f(t,c,T):
    return c*(A-T)

def rk4(c,init = Ta): #use init = 91.11 to solve for k, 98.88 when we have k and wish to find the other required information
    T91 = t91 = T120 = t120 = T44 = t44 = 0
    #specific values used to find out time occurences of some temperature
    #T values not needed, but useful to check that t value correspondence is correct
    i = 0
    T[i] = init
    while T[i] >= 44:
        if (init == T0):
            if (T91 == 0 and 91.10 < T[i] < 91.12):
                T91 = T[i]
                t91 = t[i]
            if (t120 == 0 and 66.659 < T[i] < 66.66):
                T120 = T[i]
                t120 = t[i]

        else:
            T91 = Ta
            t91 = 0
            if (t120 == 0 and 119.99999 < t[i] < 120.1):
                T120 = T[i]
                t120 = t[i]

        if (t44 == 0 and 44.439 < T[i] < 44.441):
            T44 = T[i]
            t44 = t[i]

        k1 = f(t[i], c, T[i])
        k2 = f(t[i] + .5*h, c, T[i] + .5*h*k1)
        k3 = f(t[i] + .5*h, c, T[i] + .5*h*k2)
        k4 = f(t[i] + h, c, T[i] + h*k3)

        m = 1/6 * (k1 + 2*(k2 + k3) + k4)

        t[i+1] = t[i] + h
        T[i+1] = T[i] + m

        i += 1
    return t, T, T91, t91, T120, t120, T44, t44

def temps(c):
    return rk4(c)[4]
c1 = 10 ** (-5.3)
c2 = 10 ** (-5.325)
c3 = 10 ** (-5.35)

T1 = temps(c1)
T2 = temps(c2)
T3 = temps(c3)

# print(T1)
# print(T2)
# print(T3)

cval = np.array([c1,c2,c3])
Tval = np.array([T1,T2,T3])

def interp(u,v,n): #arr = xl and n = 2 for 2nd order
    rows = cols = n+1
    mat = np.zeros((rows,cols)) #empty matrix to store elements for interpolation matrix
    for i in range(rows):
        for j in range(cols):
           mat[i][j] = u[i]**(n-j)
    return inv(mat).dot(v)


coeffs = interp(cval,Tval,2)
print(coeffs)
coeffs[2] -= 66.66
k_estm = np.roots(coeffs)[1]
#print(k_estm)
print(rk4(k_estm))

Tfin = rk4(k_estm,T0)
print(Tfin) ##Prints time and temperature array, time and temperature for 91.11F, 66.66F, and 44.44F