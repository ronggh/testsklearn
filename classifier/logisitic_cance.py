import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.externals import joblib


def logisitic_cancer():
    """
    逻辑回归预测癌症良性/恶性
    :return: None
    """
    # 1、数据获取（因为数据和属性描述分开的，需要加上names)
    path = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"
    column_names = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
                    'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
                    'Normal Nucleoli', 'Mitoses', 'Class']
    data = pd.read_csv(path, names=column_names)
    # print(data.head(10))

    # 2、数据处理（缺失值处理）
    # ?替换为np.nan,删除缺失样本
    data = data.replace(to_replace='?', value=np.nan)
    data.dropna(inplace=True)

    # 3、数据集划分
    # 3.1 筛选特征值与目标值,特征：行全保留,列从左边第一列（默认从0开始算）起，到右边第二列（负数表示从右边数起）
    x = data.iloc[:, 1:-1]
    y = data["Class"]
    # print(x.head(10))
    # print(y.head(10))
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=22)

    # 4、特征工程（数据标准化处理）
    ss = StandardScaler()
    x_train = ss.fit_transform(x_train)
    x_test = ss.transform(x_test)

    # 5、逻辑回归处理器
    estimator = LogisticRegression()
    estimator.fit(x_train, y_train)
    print("逻辑回归-回归系数：\n", estimator.coef_)
    print("逻辑回归-偏置：\n", estimator.intercept_)

    # 模型的保存和重新加载
    joblib.dump(estimator, "./logistic_cancer.pkl")
    # estimator = joblib.load("./logistic_cancer.pkl")

    # 6、模型评估
    # 得出预测结果
    y_predict = estimator.predict(x_test)
    print("预测值为:\n", y_predict)

    # 得出预测的准确率
    print("预测的准确率为：\n", estimator.score(x_test, y_test))

    # 查看精确率、召回率与F1-Score
    report = classification_report(y_test, y_predict, labels=[2, 4], target_names=['2-良性', '4-恶性'])
    print("精确率、召回率与F1-Score:\n", report)

    # roc_auc_score()要求：每个样本的真实类别，必须为0（反例），1（正例）标记，因此，需要进行转换
    y_true = np.where(y_test > 3, 1, 0)
    ras = roc_auc_score(y_true, y_predict)
    print("roc_auc:\n", ras)

    return None


if __name__ == "__main__":
    logisitic_cancer()