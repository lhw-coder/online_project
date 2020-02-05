import numpy as np
import math
import matplotlib.pyplot as plt

x = np.linspace(-5,5,200)
y = [1/(1+math.e**(-x)) for x in x]
plt.plot(x,y)
plt.show()

a = np.linspace(-60,60,200)
b = [1/(1+math.e**(-a)) for a in a]
plt.plot(a,b)
plt.show()