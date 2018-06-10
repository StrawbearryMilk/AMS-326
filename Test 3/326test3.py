import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

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

initValue = 10000000
finalValue = 100000000000

def nhaGrowth(mu, sigma=0.001473, n=3380):
    i = 0
    z = bmTransform(0.4369, 0.2210, 0.5916, 0.7787, n)

    s = normalTransform(mu,sigma,z)
    currValue = np.zeros(n)
    currValue[0] = initValue

    while i < n-1:
        currValue[i+1] = currValue[i]*(1+s[i])
        i+=1
    return currValue

##Shooting method to estimate mu
g1 = .0027
g2 = .002725
g3 = .00275

gArray = np.array([g1,g2,g3])
valArray = np.array([nhaGrowth(g1)[-1], nhaGrowth(g2)[-1], nhaGrowth(g3)[-1]])

def interp(u,v,n): #used for second order interpolation
    rows = cols = n+1
    mat = np.zeros((rows,cols)) #empty matrix to store elements for interpolation matrix
    for i in range(rows):
        for j in range(cols):
           mat[i][j] = u[i]**(n-j)
    return inv(mat).dot(v)

coeffs = interp(gArray,valArray,2) #coefficients of the second order interpolation

coeffs[2] -= finalValue #shift interpolation polynomial by finalValue to find desired mu by solving quadratic equation

##1
mu_estm = np.roots(coeffs)[0]
print(mu_estm)
#Roots are 0.00271216 0.0021438
#first root is within the range .0027, .0025 so we use this point

print(nhaGrowth(mu_estm))

#2
yearEnd = np.arange(52*5, 3381, 52*5)
yearEnd -= 1
estm_Growth = nhaGrowth(mu_estm)
print(estm_Growth[yearEnd])

year = np.arange(2003,2003+13)
print(len(year))
print(year)

plt.plot(year,estm_Growth[yearEnd])
plt.title("NHA's Stock Value at the end of Each Year")
plt.ylabel("NHA's Stock Value")
plt.xlabel("Year")
plt.show()

#3
initValue = 1.66*10**12
gdpArray = nhaGrowth(mu=0.0003385, sigma=0.001414)

plt.plot(year,gdpArray[yearEnd])
plt.title("GDP Value at the end of Each Year")
plt.ylabel("GDP Value")
plt.xlabel("Year")
plt.show()

#4
found = False
a = 0
b = 3379
val = 20.2 * 10 ** 12
ep = 1*10**12 #cannot find true value so we find a neighbor instead
mid = 0
while a < b and not found:
    mid = np.floor((a+b)/2)
    if val + ep > gdpArray[mid] >= val - ep:
        found = True
    else:
        if val + ep < gdpArray[mid]:
            a = mid+1
        else: #midpoint < val
            b = mid-1
print(mid)