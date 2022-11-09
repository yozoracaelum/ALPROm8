'''
random dari numpy akan men-generate
angka acak berkisar dari 0.0 - 1.0
dalam bentuk matriks atau array
'''
import numpy as np
a = np.ones((2,3))
b = np.random.random((2,3))
print(a)
print(b)
a = 3*a
b = b+a
print(a)
print(b)