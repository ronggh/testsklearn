from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def loadiris():
    """
    加载莺尾花数据集
    :return: None
    """
    # 加载莺尾花数据集
    iris = load_iris()
    print("返回的莺尾花数据集：\n",iris)

    # 返回值是一个继承自字典的Bunch类型，可以使用字典索引或.方式引用
    data = iris["data"]
    # print("莺尾花数据的特征值：\n",data)
    # print("莺尾花数据的目标值:\n",iris.target)
    # print("莺尾花数据的特征名称:\n", iris.feature_names)
    # print("莺尾花数据的目标值名称:\n", iris.target_names)
    # print("莺尾花数据的描述:\n", iris.DESCR)

    # 数据集划分
    x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,test_size=0.2,random_state=22)
    print("训练集的特征值：\n",x_train)
    print("训练集的特征值矩阵大小：\n", x_train.shape)

    return None

if __name__=="__main__":
    loadiris()