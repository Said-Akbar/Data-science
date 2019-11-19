# 11/19/2019 created by SaidakbarP
# Matrix. Solution sets. Some matrix equations do not have solutions. because they do not have inverse, or do not overlap

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 1000)
y1 = 5/4 - 2*x # 8x+4y=5 => y=5/4-2x
y2 =5/2 - 2*x # 4x+2y=5 => y=5/2-2x
plt.plot(x, y1, c='blue')
plt.plot(x, y2, c= 'blue')
plt.show()

# homogeneous square matrix is a matrix with constant vectors all zeros. It can have many solutions and always have zero as a trivial solution.

def test_homog(x3):
    x1 = 4/3 * x3
    x2 = 0
    if 6*x1+10*x2-8*x3==0 and -6*x1-4*x2+8*x3==0:
        return True
    return False
b_one = test_homog(1)
b_two = test_homog(-10)
