#Jeffrey Rodriguez 110733867
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

#Interpolation of left side
xl = np.array([-1,-.75,-.5,-.25,0])
xr = np.array([0,.25,.5,.75,1])
xlr = np.unique(np.append(xl,xr)) #array of left and right values
print(xlr)
def f(x):
    return (1+25*x**2)**(-1)
yl = f(xl)
yr = yl[::-1]
def interp(u,v,n): #arr = xl and n = 4 for 4th order
    rows = cols = n+1
    mat = np.zeros((rows,cols)) #empty matrix to store elements for interpolation matrix
    for i in range(rows):
        for j in range(cols):
           mat[i][j] = u[i]**(n-j)
    return inv(mat).dot(v)

def quadReg(u,v):
    X = np.zeros((3,3))
    Y = np.zeros(3)
    X[0][0] = len(u)
    X[0][1] = X[1][0] = sum(u)
    X[0][2] = X[1][1] = X[2][0] = sum(u**2)
    X[1][2] = X[2][1] = sum(u**3)
    X[2][2] = sum(u**4)

    Y = np.array([sum(v),sum(u*v),sum(u**2 * v)])
    return inv(X).dot(Y)

a = interp(xl,yl,4)
b = quadReg(xr,yr)

print("a below")
print(a) ##Use this to get coefficients for interpolation function
print(b) ##Use this to get coefficients for quadratic function
def fl(t):
    return 0.42146101*t**4 + 2.51668596*t**3 + 4.56267112*t**2 + 3.42898463*t + 1
def fr(t):
    return 1.53648807*t**2 - 2.43526039*t + 0.96805247
def plotCurves():
    Xl = np.linspace(-1,0,256)
    Xr = np.linspace(0,1,256)
    X = np.linspace(-1,1,256)

    l0 = plt.plot(Xl,fl(Xl),label = '4th Order Interpolation')
    l1 = plt.plot(Xr,fr(Xr),label = 'Quadratic Fit')
    l2 = plt.plot(X,f(X),label = 'Original function')
    l3 = plt.plot(xlr,f(xlr),'ko')
    plt.title('Runge Function')

    plt.legend()
    plt.show()

plotCurves()