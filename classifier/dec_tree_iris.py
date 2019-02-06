from sklearn.tree import DecisionTreeClassifier,export_graphviz
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def dec_tree_iris():
    """
    使用决策树对鸢尾花数据集进行分类
    :return: None
    """
    # 1. 获取数据集
    iris = load_iris()
    # 2. 划分数据集
    x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,test_size=0.25,random_state=22)
    # 3. 特征工程（略,不需要）
    # ss = StandardScaler()
    # x_train = ss.fit_transform(x_train)
    # x_test = ss.transform(x_test)
    # 4. 使用决策树进行分类
    dtc = DecisionTreeClassifier(criterion='gini')
    dtc.fit(x_train,y_train)

    # 5. 评估
    y_predict = dtc.predict(x_test)
    print("预测值：\n",y_predict)
    print("比对真实值与预测值:\n",y_test == y_predict)

    # 计算准确率
    print("准确率：\n",dtc.score(x_test,y_test))

    # 可视化决策树
    export_graphviz(dtc,out_file='./iris.dot',feature_names=iris.feature_names)

    return None

if __name__ == "__main__":
    dec_tree_iris()