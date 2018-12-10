from sklearn import datasets

from sklearn.naive_bayes import GaussianNB
import pickle


if __name__ == '__main__':

    iris=datasets.load_iris()
    clf=GaussianNB()
    clf.fit(iris.data,iris.target)
    y_predict=clf.predict(iris.data)
    print(y_predict)