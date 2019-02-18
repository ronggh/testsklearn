from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.feature_extraction import  DictVectorizer
import pandas as pd

def random_forest_titanic():
    """
    随机森林结合网格搜索：分析泰坦尼克号乘客生存预测
    :return: None
    """
    # 1. 获取数据
    titanic = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
    # titanic.to_csv("./titanic.csv")

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

    # 随机森林
    rfc = RandomForestClassifier()
    # 网络搜索和交叉验证
    # 参数准备
    param_dict = {"n_estimators": [120, 200, 300, 500, 800, 1200], "max_depth": [5, 8, 10]}
    gc = GridSearchCV(rfc, param_grid=param_dict, cv=3)
    gc.fit(x_train, y_train)

    #
    y_predict = gc.predict(x_test)
    print("预测值：\n", y_predict)
    print("比对真实值与预测值:\n", y_test == y_predict)

    # 计算准确率
    print("随机森林的准确率：\n", gc.score(x_test, y_test))


    return None

if __name__ == "__main__":
    random_forest_titanic()