'''
sum() = menjumlahkan semua elemen
min() = menentukan nilai minimum
max() = menentukan nilai maksimum
'''
import numpy as np
a = np.random.random((2,3))
b = a.sum()
c = a.min()
d = a.max()
print(a)
print('Hasil Penjumlahan elemen materiks: %f ' %b)
print('Nilai minimum: %f ' %c)
print('Nilai maksimum: %f ' %d)