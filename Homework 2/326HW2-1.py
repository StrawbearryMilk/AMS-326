#Jeffrey Rodriguez 11073867
import time
start_time = time.time()


import numpy as np
import matplotlib.pyplot as plt
import texttable as tt
import math as mt
N = 100000000
M = 20000000
def randNum(a,b):
    return (a + b) % 1


interval = [i for i in range(-200,200,20)]

def get_table(bin):
    tab = tt.Texttable()
    names = ['Interval', 'Percentage']
    tab.header(names)

    tab.set_precision(5)
    for row in zip(interval,bin):
        tab.add_row(row)
    s = tab.draw()
    return s
def bigf(a,b,n): #Default N
    pBin = np.zeros(20) #percentage bin for part 2
    gBin = np.zeros(20)
    gCount = 0 #counter for each set of g numbers.
    g = 0 #used for summing gnumbers
    nums = 0 #counter which stops at N
    i = 0
    while i < n:
        g = 0
        while gCount < 20:
            x = randNum(a,b)
            y = (x*20) - 10
            z = mt.floor(y+10) #used to see which bin percentage x falls under
            pBin[z] += 1
            a = b
            b = x
            g += y
            gCount += 1
            i += 1
        gCount = 0
        gz = mt.floor((g+200)/20)
        gBin[gz] += 1
    pBin /= n
    gBin /= (n/20)
    print(pBin)
    print(np.mean(pBin)) ##1-3 ans
    print(get_table(gBin)) ##1-5
    plt.bar(interval,gBin, width=20) ##1-6
    plt.xlabel('Intervals')
    plt.ylabel('Percentage')
    plt.title('Percentage of g Numbers in Each Sub-Interval')
    plt.show()

def bmTransform(a,b,c,d,n):
    i = 0
    z = []
    ghost = []
    while i < n:
        x = randNum(a,b)
        y = randNum(c,d)
        z1 = mt.sqrt(-2*mt.log(x))*mt.cos(2*mt.pi*y)
        z2 = mt.sqrt(-2*mt.log(x))*mt.sin(2*mt.pi*y)
        a = b
        b = x

        c = d
        d = y
        if z1 < -5 or z1 > 5:
            ghost.append(z1)
        else:
            z.append(z1)
        if z2 < -5 or z2 > 5:
            ghost.append(z2)
        else:
            z.append(z2)
        i+=2
    if len(ghost) != 0:
        print(ghost)
    print(n)
    plt.hist(z, range=(-5, 5), normed=False, bins=30)
    plt.xlabel('Box-Mueller Transformed Numbers')
    plt.ylabel('Amount')
    plt.show()

#Uncomment to see the outputs.

#bigf(0.396184,0.265781,100000000)
#bmTransform(0.396184,0.265781,0.221573,0.665431,M)

print(str(time.time() - start_time) + " secs to run")