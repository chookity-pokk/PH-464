"""
Name: Hank Greenburg
Class: PH 464
Date: 9/27/2019

Python experience comes from PH36x and the PH21x series at Linn Benton as well
as my job which is data analysis at the national energy technology lab.
I had to look up Bisection Method via wikipedia @ https://en.wikipedia.org/wiki/Bisection_method

"""
from math import cos
import numpy as np
import matplotlib.pyplot as plt

delta = 0.1

def myinterval():
    lowerbound = 0.0
    upperbound = 1.0
    return lowerbound, upperbound

def myfunction(x):
    return np.cos(x) - x

def find(lowerbound,upperbound):
    bisect = (lowerbound + upperbound) / 2
    value = myfunction(bisect)
    lower = myfunction(bisect)
    upper = myfunction(bisect)
    if (abs(value) < delta):
        return bisect
    if lower < 0 and value > 0:
        return find(bisect, lower)
    return find(bisect, upperbound)

point = find(*myinterval())

print('Zero @ ', point)

rangee = np.arange(0,1,delta)
total_range = myfunction(rangee)

plt.plot(rangee,total_range)
plt.scatter(point, myfunction(point))
plt.ylabel('f(X)')
plt.xlabel('x')
plt.show()
