# 11/18/2019 created by SaidakbarP
# Matrix Algebra
# We can use matrix algebra to figure out coefficients of linear functions. We learn about dot product and determinant in this lesson.
import numpy as np
import matplotlib.pyplot as plt

# dot product
matrix_a = np.asarray([
    [0.7, 3, 9],
    [1.7, 2, 9],
    [0.7, 9, 2]
], np.float32)
vector_b = np.asarray([
    [1],[2],[1]
])
ab_product = np.dot(matrix_a, vector_b)
print(ab_product)

# ab and ba not the same in matrix multiplication
matrix_a = np.asarray([
    [0.7, 3],
    [1.7, 2],
    [0.7, 9]
], dtype=np.float32)

matrix_b = np.asarray([
    [113, 3, 10],
    [1, 0, 1],
], dtype=np.float32)

product_ab = np.dot(matrix_a, matrix_b)
product_ba = np.dot(matrix_b, matrix_a)

print('ab and ba are not the same:\n', product_ab,'\n\n', product_ba)

matrix_a = np.asarray([
    [0.7, 3],
    [1.7, 2],
    [0.7, 9]
], dtype=np.float32)

matrix_b = np.asarray([
    [113, 3, 10],
    [1, 0, 1],
], dtype=np.float32)

# transpose
transpose_a = np.transpose(matrix_a)
print(matrix_a)
print(np.transpose(transpose_a))
trans_ba = np.dot(np.transpose(matrix_b),transpose_a)
trans_ab = np.dot(transpose_a,np.transpose(matrix_b))
product_ab = np.dot(matrix_a, matrix_b)
print(np.transpose(product_ab))
print(trans_ba)

# identity matrix
i_2 = np.identity(2)
i_3 = np.identity(3)
matrix_33 = np.asarray([[1,2,3], [1,2,3], [1,2,3]], np.float32)
matrix_23 = np.asarray([[1,2,3], [1,2,3]], np.float32)
identity_33 = np.dot(i_3, matrix_33)
identity_23 = np.dot(i_2, matrix_23)
print(identity_33, '\n', matrix_33)
print(identity_23, '\n', matrix_23)

# inverse of matrix
matrix_a = np.asarray([
    [1.5, 3],
    [1, 4]
])

def matrix_inverse_two(mat):
    det = mat[0,0]*mat[1,1]-mat[0,1]*mat[1,0]
    if det==0: return False
    right_mat = np.asarray([[mat[1,1], -mat[0,1]], 
                           [-mat[1,0], mat[0,0]]])
    return np.dot(1/det, right_mat)
inverse_a = matrix_inverse_two(matrix_a)
i_2 = np.dot(inverse_a, matrix_a)
print(i_2)

# using numpy library
solution_x = np.dot(
    np.linalg.inv(np.asarray([[30,-1],
                              [50, -1]])), 
				np.asarray([[-1000],[-100]]))

# finding the determinant with numpy				
matrix_22 = np.asarray([
    [8, 4],
    [4, 2]
])

matrix_33 = np.asarray([
    [1, 1, 1],
    [1, 1, 6],
    [7, 8, 9]
])

det_22 = np.linalg.det(matrix_22)
det_33 = np.linalg.det(matrix_33)
