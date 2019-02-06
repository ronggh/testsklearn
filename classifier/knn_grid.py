from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler


import pandas as pd

def knncls():
    """
    kNN - k近邻分类，来预测
    :return: None
    """
    # 1. 使用pandas 读取数据
    data = pd.read_csv("../data/FBlocation/train.csv")
    # print(data.head(10))

    # 2. 处理数据
    # 2.1 缩写数据范围
    data = data.query("x < 2.5 & x > 2 & y < 1.5 & y > 1.0")
    # 2.2 处理时间
    time_value = pd.to_datetime(data['time'], unit='s')
    # print(time_value)
    # 把日期格式转换成 字典格式
    time_value = pd.DatetimeIndex(time_value)

    # 构造一些新特征
    data['day'] = time_value.day
    data['hour'] = time_value.hour
    data['weekday'] = time_value.weekday

    # 把原数据集中的时间戳特征删除，按列方式删除
    data = data.drop(['time'], axis=1)
    # 2.3 把签到数量小于n个目标位置删除
    place_count = data.groupby('place_id').count()
    # print(place_count)
    # 只保留签到次数大于3的place_id,重新进行索引
    tf = place_count[place_count.row_id > 3].reset_index()
    # print(tf)
    # 过滤数据
    data = data[data['place_id'].isin(tf.place_id)]
    # 删除无用的row_id,否则会对预测结果产生影响
    # 删除并特征化数据后，准确率37%
    data = data.drop(['row_id'],axis=1)

    # 2.4 取出数据集中的目标值和特征值
    y = data['place_id']
    x = data.drop(['place_id'],axis=1)

    # 进行数据集的划分，分为训练集和测试集
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)

    # 3. 进行特征工程，数据标准化
    # 不进行标准化，在保留row_id的情况下，准确率只有0.5%左右
    # 特征化后，准确率提高到25%
    # 只需要对训练集和测试集的特征集进行标准化
    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    # 测试集可以只进行transform,因为是和训练集同样的fit()数据
    x_test = std.transform(x_test)

    # KNN算法流程
    knn = KNeighborsClassifier()
    # 设置参数值
    param = {"n_neighbors":[3,5,7]}
    # 进行网格搜索
    gc = GridSearchCV(knn,param_grid=param,cv=10)
    gc.fit(x_train,y_train)
    # 预测准确率
    print("在测试集上的准确率:\n",gc.score(x_test,y_test))
    print("在交叉验证中的最好结果：\n",gc.best_score_)
    print("最好的模型是：\n",gc.best_estimator_)
    print("每次交叉验证的结果:\n",gc.cv_results_)

    return None

if __name__ =="__main__":
    knncls()