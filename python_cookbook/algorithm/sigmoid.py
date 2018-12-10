import numpy as np
import matplotlib.pyplot as plt

size=50
x1=np.linspace(0,10,size)+np.random.rand(size)*5
y1=2*x1+1+np.random.rand(size)*5


x2=np.linspace(0,10,size)+np.random.randn(size)*1
y2=2*x2+10+np.random.randn(size)*1

plt.figure()
plt.scatter(x1,y1,color='r',marker='s')
plt.scatter(x2,y2,color='b',marker='o')
plt.show()
