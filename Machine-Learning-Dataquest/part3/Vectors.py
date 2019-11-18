# 11/17/2019 created by SaidakbarP
# Linear Algebra
# Many real world processes can be modeled using multiple, related linear equations.
import numpy as np
import matplotlib.pyplot as plt
x =np.linspace(0,50,1000)
y1 = 30*x+1000
y2 = 50*x+100
plt.plot(x,y1, color='orange')
plt.plot(x,y2, color='blue')

# Many real world systems are modeled using many more than 2 variables and functions and solving by hand is unfeasible
# We use Gaussian elimination to solve complex matrix problems
# create a matrix:
import numpy as np
matrix_one = np.asarray([
    [30, -1, -1000],
    [50, -1, -100]
    ], np.float32)
# operations on matrix	
matrix_one = np.asarray([
    [30, -1, -500],
    [50, -1, -100]  
], dtype=np.float32)

matrix_one[0]=matrix_one[0]/30

# solving by elimination
matrix_three = np.asarray([
    [1, -1/30, -1000/30],
    [0, 1, 2350]  
], dtype=np.float32)
matrix_three[0] = matrix_three[0]+matrix_three[1]/30 # this makes the first row [1,0,?]

# vectors
plt.quiver(0,0,2,3, angles = 'xy', scale_units = 'xy', scale=1, color='blue') # start x, start y, end x, end y.
plt.quiver(0,0,-2,-3, angles = 'xy', scale_units = 'xy', scale = 1, color='blue')
plt.quiver(0,0,1,1, angles='xy', scale_units='xy', scale=1, color='gold')
plt.quiver(0,0,2,2, angles='xy', scale_units='xy', scale=1, color='gold')

plt.axhline(0, c='black', lw=0.5)
plt.axvline(0, c='black', lw=0.5)
plt.xlim(-3,3)
plt.ylim(-4,4)
plt.show()

# vector addition

plt.axhline(0, c='black', lw=0.5)
plt.axvline(0, c='black', lw=0.5)
plt.xlim(-4,4)
plt.ylim(-1,4)

plt.quiver(0,0,3,0, angles='xy', scale_units='xy', scale=1)
plt.quiver(3,0,0,3, angles='xy', scale_units='xy', scale=1)
plt.quiver(0,0,3,3,angles='xy', scale_units='xy', scale=1, color='green')
plt.show()

# scalar multiplication
plt.axhline(0, c='black', lw=0.5)
plt.axvline(0, c='black', lw=0.5)
plt.xlim(0,10)
plt.ylim(0,5)

plt.quiver(0,0,3,1, angles='xy', scale_units='xy', scale=1, color='blue')
plt.quiver(0,0,6,2, angles='xy', scale_units='xy', scale=1, color='green')
plt.quiver(0,0,9,3, angles='xy', scale_units='xy', scale=1, color='orange')
plt.show()

# matrix operations with numpy
vector_one = np.asarray([
    [1],
    [2],
    [1]
], dtype=np.float32)
vector_two = np.asarray([[3],[0], [1]], dtype=np.float32)
vector_linear_combination = vector_one*2 + vector_two*5

# dot product
vector_one = np.asarray([
    [1],
    [2],
    [1]
], dtype=np.float32)

vector_two = np.asarray([
    [3],
    [0],
    [1]
], dtype=np.float32)

dot_product = np.dot(vector_one[:,0], vector_two)
print(dot_product)

w = np.asarray([
[1],[2]
], np.float32)
v = np.asarray([
[3], [1]
], np.float32)
end_point = v*2-2*w


