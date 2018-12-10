import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


x=np.linspace(0,6.3,100)
y=np.sin(x)+np.random.rand(x.shape[0])/2

# plt.figure()
plt.scatter(x,y)
plt.show()