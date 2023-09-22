import numpy as np
N = int(input())
M = int(input())
c = 3
matrix = np.zeros((N, M))
count = 1
for i in range(N):
    for q in range(M):
        matrix[i][q] = count
        count += 1
for i in range(N):
    if i % 2 == 1:
        matrix[i] = matrix[i][::-1]
print(matrix)
