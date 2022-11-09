'''
arange(a,b,c)
a = nilai awal
b = nilai akhir
c = step / langkah
reshape(a,b)
a = row
b = column
'''
import numpy as np
a=np.arange(15).reshape(3,5)
print(a)
print('Baris dan Kolom matrik adalah : ',a.shape)
print('Dimensi Matrik adalah : ',a.ndim)
print('Ukuran byte setiap elemen Matrik adalah : ',a.itemsize)
print('Jumlah elemen Matrik adalah : ',a.size)