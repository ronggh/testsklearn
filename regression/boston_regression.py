from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,SGDRegressor,Ridge
from sklearn.metrics import mean_squared_error

def linear_regression_boston():
    """
    ，预测波士顿房价
    :return: None
    """
    # 1、获取数据
    boston = load_boston()
    # 2、数据集划分
    x_train,x_test,y_train,y_test = train_test_split(boston.data,boston.target,test_size=0.25,random_state=22)
    # 3、特征工程(标准化),对特征值和目标值都需要做标准化处理
    ss_x = StandardScaler()
    x_train = ss_x.fit_transform(x_train)
    x_test = ss_x.transform(x_test)
    # StandardScaler要求数据必须是二维的，目标值如果是一维的，需要进于转换成
    ss_y = StandardScaler()
    y_train = ss_y.fit_transform(y_train.reshape(-1,1))
    y_test = ss_y.transform(y_test.reshape(-1,1))

    # 4.1 、预估器流程——正规方程优化算法
    lr = LinearRegression(fit_intercept=True)
    lr.fit(x_train,y_train)
    # 4.2 、得出模型
    print("正规方程-回归系数：\n",lr.coef_)
    print("正规方程-偏置：\n",lr.intercept_)
    # 4.3 、模型评估,因为进行过标准化， 真实值需要进行转换
    y_predict_lr = ss_y.inverse_transform(lr.predict(x_test))
    #print("正规方程-预测值：\n",y_predict_lr)
    # 需要转换成标准化前的值来计算误差
    mse_lr = mean_squared_error(ss_y.inverse_transform(y_test),y_predict_lr)
    print("正规方程--误差：\n",mse_lr)

    # 5.1 、预估器流程——梯度下降
    sgd = SGDRegressor(learning_rate='constant', eta0=0.01, max_iter=10000)
    sgd.fit(x_train, y_train)
    # 5.2、得出模型
    print("梯度下降-回归系数：\n", sgd.coef_)
    print("梯度下降-偏置：\n", sgd.intercept_)
    # 5.3、模型评估,得出预测值，因为进行过标准化， 值需要进行转换
    y_predict_sgd = ss_y.inverse_transform(sgd.predict(x_test))
    #print("梯度下降-预测值：\n", y_predict_sgd)
    # 需要转换成标准化前的值来计算误差
    mse_sgd = mean_squared_error(ss_y.inverse_transform(y_test), y_predict_sgd)
    print("梯度下降--误差：\n", mse_sgd)

    # 6.1 、预估器流程——岭回归
    ridge = Ridge()
    ridge.fit(x_train, y_train)
    # 6.2、得出模型
    print("岭回归-回归系数：\n", ridge.coef_)
    print("岭回归-偏置：\n", ridge.intercept_)
    # 5.3、模型评估,得出预测值，因为进行过标准化， 值需要进行转换
    y_predict_ridge = ss_y.inverse_transform(ridge.predict(x_test))
    #print("岭回归-预测值：\n", y_predict_ridge)
    # 需要转换成标准化前的值来计算误差
    mse_ridge = mean_squared_error(ss_y.inverse_transform(y_test), y_predict_ridge)
    print("岭回归--误差：\n", mse_ridge)

    return None


if __name__ == "__main__":
    # 线性回归，预测波士顿房价
    linear_regression_boston()

