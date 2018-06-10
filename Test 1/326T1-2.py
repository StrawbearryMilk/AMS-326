#Jeffrey Rodriguez
#AMS326 Test 1-2
import math as mt

def sameSign(a,b):
    return a * b > 0
def bisection(a,b):
    epsilon = 0.000001
    count = 0 #used to count number of iterations
    while count < 50: #arbitrary "big" number to prevent large loop
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
    print("Xn = " + str(m) + " and there were " + str(count) + " interations.")
    return m
#roots 2 and 3 bisection(4.485,4,495), bisection(-4.485,-4,495)
#roots 3 and 4, bisection(7.65,7.75), bisection(-7.65,-7.75)