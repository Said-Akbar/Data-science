# 11/17/2019 created by SaidakbarP
# Understanding the LIMITS
# KNN is a compute intensive task. IT calculates the distance of each new observation by averaging the distance from each train observation
# Instead of KNN, we can use a linear function. y=mx+b. m is a slope while b is an intercept.

# here is the simple slope calculator function for two given point coordinates
import numpy as np
import matplotlib.pyplot as plt
def slope(x1,x2,y1,y2):
    return (y1-y2)/(x1-x2)
	
slope_one = slope(0,4,1,13)
slope_two = slope(5,-1,16,-2)

# linear function only represents a straight line. If we want more flexibility we can add more degrees of power to the function.
# one example is a quadratic function.
# secant line is a line that intersects with 2 points in a non-linear function graph.
import seaborn
seaborn.set(style='darkgrid')

def draw_secant(x1,x2):
    x = np.linspace(-20,30,100)
    y = -1*(x**2) + x*3 - 1
    plt.plot(x,y)
	
    y1 = -1*(x1**2) + x1*3 - 1 # this is our quadratic function
    y2 = -1*(x2**2) + x2*3 - 1
    m = (y2-y1)/(x2-x1)
	
    b = y1-x1*m
    ysec = x*m+b # our secant line function
    plt.plot(x,ysec)
    plt.show()
    
draw_secant(3,5)
draw_secant(3,10)
draw_secant(3,15)

#Sympy is a symbolic python library for calculating limits.

import sympy
x2, y = sympy.symbols('x2 y') # declare sympy symbols.
limit_one = sympy.limit((-x2**2+3*x2-1+1)/(x2-3), x2, 2.9) # first: limit function; second: variable in the limit function; third: the number the limit is approaching.

