import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np

if __name__ == '__main__':
    x = np.array([50, 100, 150, 200, 250, 300]).reshape(6, 1)
    y = np.array([150, 200, 250, 280, 310, 330])
    plt.plot(x, y)

    lr = LinearRegression()
    lr.fit(x, y)

    x1 = np.array([30, 400]).reshape(2, 1)
    y1=lr.predict(x1)
    plt.plot(x1,y1)

    pr=PolynomialFeatures(degree=3)
    pr.fit_transform(x,y)
    pr.
    plt.show()
