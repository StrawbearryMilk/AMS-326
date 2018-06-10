import math as mt
import numpy as np
import matplotlib.pyplot as plt

#Jeffrey Rodriguez 110733867
#AMS326 HW#1

# 1-1 [Uncomment functions below for output]
def sig(x):
    return (1 + np.exp(-x))**(-1) #Add = 1, exp ~ 4, inversion ~4, 9 flops per call

def dx(a, b, n):
    return (b - a)*1/n #1 + 4

def rectangle(a,b,n):
    h = dx(a,b,n) #5 flops
    x = np.linspace(a, b, num = n, endpoint = False) #n addition + n multiplication = 2n flops
    value = np.sum(sig(x)) #sum sig(a) to sig(n-1), (n-1)*9n flops
    return h*value #1 flops

def trapezoid(a,b,n):
    x = np.linspace(a, b, num = n, endpoint = False) #n addition + n multiplication = 2n
    h = dx(a,b,n) #5
    m = .5*(sig(a) + sig(b)) #9*2 + 1
    return h*(m + np.sum(sig(x[1:n]))) #1 + (1 + 9(n-1)*(n-2))

#rectangle(-4, 5, 1000000)
#trapezoid(-4, 5, 1000000)

########################################################################
#1-2 [Uncomment functions below for output]
def graph(function, domain): #graph function used to determine roots of function.
    x = np.linspace(0,2,256, endpoint=True)
    y = eval(function)
    plt.plot(x,y, linewidth = 1, linestyle = "-")
    plt.gca().xaxis.grid(True)
    plt.gca().yaxis.grid(True)
    plt.show()

#Guess x1 = 1.51, delta = .01 based on graph
#f[x1-delta]=-0.7196, f[x1+delta] = 0.0323

def f(x):
    return 2.018 ** (-x ** 3) - (x ** 4) * mt.sin(x ** 3) - 1.984
x1 = 1.51
delta = 0.01
epsilon = 0.0000001

def sameSign(a,b):
    return a * b > 0

def bisection(a,b,limit,epsilon = 10**(-7)):
    count = 0 #used to count number of iterations
    while count < limit: #arbitrary number to prevent large loop
        m = (a+b)/2
        if mt.fabs(f(m)) <= epsilon:
            break
        elif sameSign(f(a),f(m)):
            a = m
        elif sameSign(f(b),f(m)):
            a = a
            b = m
        count += 1
        #print(m)
    print("Xn = " + str(m) + " and there were " + str(count) + " iterations.")
    return m


#graph('2.018**(-x**3) - (x**4) * np.sin(x**3) - 1.984',range(0,2))
#bisection(1.50,1.51,limit = 50)