'''
zeros() = semua elemen dari matriks bernilai 0
ones() = semua elemen dari matriks bernilai 1
linspace(a,b,c)
a = nilai awal
b = nilai akhir
c = banyaknya elemen dengan step yang sama rata
linspace(0,20,5)
[ 1.    5.75 10.5  15.25 20.  ]
linspace(0,20,7)
[ 1.          4.16666667  7.33333333 10.5        13.66666667 16.83333333
 20.        ]
'''
import numpy as np
a=np.zeros((3,4))
b=np.ones((3,4))
c=np.linspace(1,20,7)
print(a)
print(b)
print(c)