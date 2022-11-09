'''
inv() => menentukan matriks invers
numpy.linalg.inv()
A * A^-1 = I
'''
import numpy as np
x = np.array([[1,2],[3,4]])
y = np.linalg.inv(x)
print (x)
print (y)
print (np.dot(x,y))