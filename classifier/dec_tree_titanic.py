from sklearn.tree import DecisionTreeClassifier,export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import  DictVectorizer
import pandas as pd

def dec_tree_titanic():
    """
    决策树分析泰坦尼克号乘客生存预测
    :return: None
    """
    # 1. 获取数据
    titanic = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")

    # 选取特征值、目标值
    x = titanic[["pclass","age","sex"]]
    y = titanic["survived"]

    # 数据处理（缺失值补全、字典值one-hot编码）
    # 对age进行缺失值处理，对pclass,sex进行one-hot编码
    x["age"].fillna(x["age"].mean(),inplace=True)
    x = x.to_dict(orient="records")

    # 划分数据集（训练集、测试集）
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=22)
    # 特征工程（字典特征抽取）
    dv = DictVectorizer()
    x_train = dv.fit_transform(x_train)
    x_test = dv.transform(x_test)

    # 决策树预估器
    dtc = DecisionTreeClassifier(criterion='gini',max_depth=8)
    dtc.fit(x_train, y_train)

    # 5评估
    y_predict = dtc.predict(x_test)
    print("预测值：\n", y_predict)
    print("比对真实值与预测值:\n", y_test == y_predict)

    # 计算准确率
    print("准确率：\n", dtc.score(x_test, y_test))

    # 可视化决策树
    export_graphviz(dtc, out_file='./dec_tree_titanic.dot', feature_names=dv.get_feature_names())


    return None

if __name__ == "__main__":
    dec_tree_titanic()