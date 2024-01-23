import numpy as np
import matplotlib.pyplot as plt

n = [x for x in range(100000)]

t2 = n*np.log(n)

t3 = [x*4+1 for x in n]

t4 = [x*6-5 for x in n]

plt.plot(n, t2, label = "t2")
plt.plot(n, t3, label = "t3")
plt.plot(n, t4, label = "t4")

plt.legend()
plt.show()