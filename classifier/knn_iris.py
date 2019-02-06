from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

def knn_iris():
    """
    KNN分类预测鸢尾花数据集
    :return:None
    """
    #  1、获取数据
    iris = load_iris()

    # 2、划分数据集
    x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,test_size=0.25,random_state=22)

    # 3、特征工程（标准化）
    ss= StandardScaler()
    x_train = ss.fit_transform(x_train)
    x_test = ss.transform(x_test)

    # 4、KNN预测
    estimator = KNeighborsClassifier(n_neighbors=5,algorithm='auto')
    estimator.fit(x_train,y_train)

    # 5、评估
    # 5.1 方法一：
    y_predict = estimator.predict(x_test)
    print("预测值：\n",y_predict)
    print("真实值与预测值比对：\n", y_test == y_predict)
    # 方法二：
    print("准确率：\n",estimator.score(x_test,y_test))

    return None

if __name__ == "__main__":
    knn_iris()