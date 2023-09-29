import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

pos = 0
scale = 10
size = 10000000
s2 =1000
v1 = np.random.normal(pos, scale, size)
v2 = np.random.normal(pos, scale, s2)
ax1.hist(v1, 100)
ax2.hist(v2, 100)
plt.show()
