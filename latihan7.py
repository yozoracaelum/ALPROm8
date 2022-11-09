'''
A = [[a,b],
     [c,d]]
B = [[e,f],
     [g,h]]
A * B
[[a*e, b*f],
 [c*g, d*h]]
dot() => numpy
A x B
1) A.dot(B)
2) numpy.dot(A,B)
'''
import numpy as np
A = np.array([[1,1],
              [0,1]])
B = np.array([[2,0],
              [3,4]])
C = A*B
print(C)
D = A.dot(B)
print(D)
E = np.dot(A,B)
print(E)