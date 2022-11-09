'''
det() => determinan
numpy.linalg.det()
linalg => linear algebra
'''
import numpy as np
b = np.array([[6,1,1], [4, -2, 5], [2,8,7]])
print (b)
print ('\n Determinan Matriks adalah: %.2f' %np.linalg.det(b))