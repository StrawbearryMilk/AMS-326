#Jeffrey Rodriguez 110733867

import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
import texttable as tt
from scipy import stats
from scipy.stats import itemfreq

x = np.array([1,2,3,4,5])
y = np.array([6967,7115,7051,6777,6874]) #values gathered from Yahoo's finance page, decimals dropped
dates = (['2/5','2/6','2/7','2/8','2/9'])

def interp(u,v,n): #arr = x and n = 4 for 4th order
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

def getCoeffs(a,b):
    return inv(a).dot(b)

a = interp(x,y,4)
b = quadReg(x,y)
print(a)
print(b)
def f1(t):
    return 24.125*t**4 - 240.91666667*t**3 + 736.375*t**2 - 736.58333333*t + 7184
def f2(t):
    return( -22.28571429*t**2 + 81.31428571*t + 6958)

def plotCurves(x=x,y=y): #takes in x and y vectors, and computed coefficients
    X = np.linspace(1, 5, 256)
    l0 = plt.plot(x,y,'co',label = 'Original data')
    l1 = plt.plot(X,f1(X),label = '4th Order Interpolation')
    l2 = plt.plot(X,f2(X),label = 'Quadratic Interpolation')
    plt.xticks(x,dates)
    plt.xlabel('First Week of February 2018')
    plt.ylabel('Closing Values of NASDAQ Index')
    plt.title('NASDAQ Index Closing Values in the First Week of February 2018')

    plt.legend()
    plt.show()
plotCurves()
