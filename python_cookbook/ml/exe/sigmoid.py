import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(-10,10,100)
y1= (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
y2= (1) / (1 + np.exp(-x))

plt.figure()
plt.plot(x, y1,color='red')
plt.plot(x, y2,color='blue')
plt.show()
