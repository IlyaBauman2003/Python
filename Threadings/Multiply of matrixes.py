import numpy as np
import pandas as pd
import threading
from time import time

def C_ij(i, j, k):
    for _k in range(k):
        C[i,j] += A[i,_k] * B[_k,j]

n,k, m = map(int, input("Enter n, k, m (matrixes n*k and k*m): ").split())

A = np.random.randint(n*k, size = n*k).reshape(n, k)
B = np.random.randint(k*m, size = k*m).reshape(k, m)
C = np.zeros((n, m))

Threads = []

start = time()
for i in range(n):
    for j in range(m):
        thr = threading.Thread(target = C_ij, args = (i,j,k))
        thr.start()
        Threads.append(thr)

for Thr in Threads:
    Thr.join()
time_par = time() - start

print("Matrix A")
print()
print(pd.DataFrame(A))
print("Matrix B")
print()
print(pd.DataFrame(B))
print()
print("Matrix C")
print()
print('Dot of matrixes: {:.2f} seconds taken'.format(time_par))
print(pd.DataFrame(C))
