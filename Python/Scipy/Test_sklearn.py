#!/usr/bin/env python

import unittest

# 以下练习是跟着周莫烦在Youtube 上的 sklearn 教程的练习内容


class Test_Sklearn_ZMF(unittest.TestCase):

    # 跟着[http://youtu.be/EvV99YhSsJU] 教程进行练习
    def n_test_L4(self):
        import numpy as np
        from sklearn import datasets  # sklearn 自带数据集
        from sklearn.cross_validation import train_test_split
        from sklearn.neighbors import KNeighborsClassifier

        iris = datasets.load_iris()  # iris 是一种花
        iris_X = iris.data
        iris_y = iris.target

        # print(type(iris))
        # print(iris_X)
        # print(iris_y)

        X_train, X_test, y_train, y_test = train_test_split(
            iris_X, iris_y, test_size=0.3)

        knn = KNeighborsClassifier()
        knn.fit(X_train, y_train)
        pre_result = knn.predict(X_test)
        print(X_test)
        for x, y in zip(pre_result, y_test):
            self.assertEqual(x, y, msg="{} != {}".format(x, y))

    def n_test_L5(slef):
        from sklearn import datasets
        from sklearn.linear_model import LinearRegression
        import matplotlib.pyplot as plt
        import numpy as np

        loaded_data = datasets.load_boston()
        X_data = loaded_data.data
        y_target = loaded_data.target

        model = LinearRegression()
        model.fit(X_data, y_target)

        # print(model.predict(X_data[:4]))
        # print(y_target[:4])

        x, y = datasets.make_regression(n_samples=100, n_features=1, noise=10)
        # print(x)
        # print(y)
        # plt.scatter(x, y)
        # plt.show()
        model.fit(x, y)
        # print(model.predict([[1], [2], [3]]))

        # 构建一个数据集, y=x^2
        x = [i for i in range(100000)]
        # y = x^2 的预测很差, 改为 y= 2x+3 就准, 看来对二次方程支持不好
        # y = [ i*i for i in x ]
        y = [2 * i + 3 for i in x]

        # transpose() 对 1-D 数组不起作用
        # X = np.array(list(x)).transpose()
        X = np.array(list(x)).reshape(len(x), 1)
        # print(X)
        Y = list(y)
        # print(Y)

        model2 = LinearRegression()
        model2.fit(X, Y)

        X2 = np.array([i for i in range(0, 20)])
        print(X2)
        X2 = X2.reshape(len(X2), 1)
        print(X2)
        print(model2.predict(X2))
        print(model2.coef_)
        print(model2.intercept_)

    # L6 Model 常用属性和功能
    def test_L6(self):
        from sklearn import datasets
        from sklearn.linear_model import LinearRegression

        loaded_data = datasets.load_boston()
        X_data = loaded_data.data
        y_target = loaded_data.target

        model = LinearRegression()
        model.fit(X_data, y_target)
        print(model.coef_)
        print(model.intercept_)
        print(model.score(X_data, y_target))

    # L7 Normalization 标准化数据
    def n_test_L7(self):

        from sklearn import preprocessing
        import numpy as np
        from sklearn.cross_validation import train_test_split
        from sklearn.datasets.samples_generator import make_classification
        from sklearn.svm import SVC
        import matplotlib.pyplot as plt

        X, y = make_classification(n_samples=300, n_features=2, n_redundant=0, n_informative=2,
                        random_state=22, n_clusters_per_class=1, scale=100)

        # plt.scatter(X[:, 0], X[:, 1], y)
        # plt.show()
        X = preprocessing.scale(X)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3)
        clf = SVC()
        clf.fit(X_train, y_train)
        print(clf.score(X_test, y_test))
        plt.scatter(X[:, 0], X[:, 1], y)
        plt.show()
    
    # L8 Cross Validation 交叉验证1
    def n_test_L8(self):
        import numpy as np
        from sklearn import datasets  # sklearn 自带数据集
        from sklearn.cross_validation import train_test_split
        from sklearn.neighbors import KNeighborsClassifier

        iris = datasets.load_iris()  # iris 是一种花
        iris_X = iris.data
        iris_y = iris.target

        from sklearn.cross_validation import cross_val_score
        import matplotlib.pyplot as plt
        k_range = range(1, 31)
        k_scores = []

        for k in k_range:
            knn = KNeighborsClassifier(n_neighbors=k)
            # scores = cross_val_score(knn, iris_X, iris_y, cv=10, scoring='accuracy') # for classification
            loss = -cross_val_score(knn, iris_X, iris_y, cv=10, scoring='mean_squared_error') # for regression
            # k_scores.append(scores.mean())
            k_scores.append(loss.mean())
        
        plt.scatter(k_range, k_scores)
        plt.xlabel('Value of K for KNN')
        plt.ylabel('Cross-Validated Accuracy')
        plt.show()
    
    # L9 Cross Validation 交叉验证2
    def n_test_L9(self):
        pass
    
    def n_test_datacamp_sklearn(self):
        from sklearn import datasets
        # 載入 matplotlib
        import matplotlib.pyplot as plt
        
        # 載入 `digits`
        digits = datasets.load_digits()
        
        # 設定圖形的大小（寬, 高）
        fig = plt.figure(figsize=(4, 2))
        
        # 調整子圖形 
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
        
        # 把前 8 個手寫數字顯示在子圖形
        for i in range(8):
            # 在 2 x 4 網格中第 i + 1 個位置繪製子圖形，並且關掉座標軸刻度
            ax = fig.add_subplot(2, 4, i + 1, xticks = [], yticks = [])
            # 顯示圖形，色彩選擇灰階
            ax.imshow(digits.images[i], cmap = plt.cm.binary)
            # 在左下角標示目標值
            ax.text(0, 7, str(digits.target[i]))
        
        # 顯示圖形
        plt.show()
    


if __name__ == '__main__':
    unittest.main()
