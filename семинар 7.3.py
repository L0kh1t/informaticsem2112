import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
m = genfromtxt('iris_data.csv', delimiter=',', dtype=str)
print(m)
k = 0
b = 0
c = 0
versicolor = 0
virginica = 0
setosa = 0
for i in range(150):
    if float(m[i+1, 4]) > 1.5:
        k += 1
    elif 1.2 < float(m[i+1, 4]) <= 1.5:
        b += 1
    elif float(m[i+1, 4]) <= 1.2:
        c += 1
for i in range(150):
    if m[i+1, 5] == 'Iris-virginica':
        virginica += 1
    elif m[i+1, 5] == 'Iris-versicolor':
        versicolor += 1
    elif m[i+1, 5] == 'Iris-setosa':
        setosa += 1
print(k, b, c)
print(setosa, versicolor, virginica)
fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.pie([k, b, c], labels = ['больше 1.5','между полтора и 1.2','меньше 1.2'])
ax2.pie([setosa, versicolor, virginica], labels = ['Iris-setosa','Iris-versicolor','Iris-virginica'])
plt.show()
