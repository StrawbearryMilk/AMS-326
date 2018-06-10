#Jeffrey Rodriguez
import numpy as np
import matplotlib.pyplot as plt

def randNum(a,b):
    return (a + b) % 1

def bmTransform(a,b,c,d,n):
    i = 0
    z = np.zeros(n)
    while z[n-1] == 0: #Stop when the last entry is filled
        x = randNum(a,b)
        y = randNum(c,d)
        z1 = np.sqrt(-2*np.log(x))*np.cos(2*np.pi*y)
        z2 = np.sqrt(-2*np.log(x))*np.sin(2*np.pi*y)
        a = b
        b = x
        c = d
        d = y

        z[i] = z1
        z[i+1] = z2

        i += 2
    return z

def normalTransform(mu, sigma, arr):
    return sigma*arr + mu

initValue = 1000000
fee = 0.03333

def poorVal(mu, sigma, n, q1):
    i = 0
    if q1 is True:
        z = bmTransform(0.4369, 0.2210, 0.5916, 0.7787, n)
    else:
        z = bmTransform(0.5517, 0.3916, 0.1992, 0.3164, n)
    s = normalTransform(mu,sigma,z)
    currValue = np.zeros(n)
    currValue[0] = initValue

    while i < n-1:
        gain = currValue[i] * s[i]
        currValue[i+1] = currValue[i]*(1+s[i])
        if gain > 0:
            currValue[i+1] -= gain * fee #amount lost with each profit
        i += 1

    return currValue

def tsPlot(priceArray, q1, col, n=260):
    x = np.array(range(1,n+1))
    y = priceArray

    plt.plot(x,y,color=col)

    if q1 == True:
        plt.title("Time Series Plot Over 260 Trading Days with " r"$\mu = 0.1949\%$,$\sigma = 0.2018\%$")
    else:
        plt.title(r'Time Series Plot Over 260 Trading Days with $\mu = -0.1989\%,\sigma = 0.0640\%$')

    plt.xlabel("Trading Days")
    plt.ylabel("Investment Values")

    plt.show()

def doubleTSPlot(priceArray1, priceArray2,n=260):
    x = np.array(range(1,n+1))
    y1 = priceArray1
    y2 = priceArray2

    plt.plot(x,y1,color='blue',label = r'$\mu=0.1949\%,\sigma=0.2018\%$')
    plt.plot(x,y2,color='green',label = r'$\mu=-0.1989\%,\sigma=0.0640\%$')
    plt.title("Time Series Plots Over 260 Trading Days")

    plt.xlabel("Trading Days")
    plt.ylabel("Investment Values")

    plt.legend()
    plt.show()


invests1 = poorVal(mu=0.001949,sigma=.002018,n=260,q1=True)
invests2 = poorVal(mu=-.001989,sigma=0.00064,n=260,q1=False)

###1
tsPlot(invests1,q1=True,col='blue')

###2
tsPlot(invests2,q1=False,col='green')

##3
doubleTSPlot(invests1,invests2)

##4
print(invests1[259]) ##final price value of 1st investment
#1585602.5338004995

print(invests2[259]) ##final price value of 2nd investment
#606221.1894285457