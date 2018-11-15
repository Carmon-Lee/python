import numpy as np
import matplotlib.pyplot as plt

x = np.array([[1, 2], [3, 1], [2, 2], [4, 2]])
y = np.array([[3, 4, 5, 6]])

w = np.random.rand(2).reshape((1, 2))*0.01
b = np.zeros(1)
#
# for i in range(10000):
#     z = np.dot(w, x.T)
#     a = z
#     print(a-y)
#     da = a - y
#     dz = da
#     dw = np.mean(dz*x.T,axis=1)
#     db = np.mean(dz)
#     w -= 0.1*dw
#     b -= 0.1*db
# print(w,b)

a=np.linspace(91,100,10)
plt.figure()
plt.scatter(a,100*((1-1/a)**a-0.368)/0.368)
plt.show()
