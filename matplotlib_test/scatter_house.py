import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def scatter_house():

    # 1、准备数据
    # 房屋面积数据
    x = [225.98,247.07,253.14,457.85,241.58,301.01,20.67,288.64,163.56,120.06,207.83,342.75,147.9,53.06,224.72,29.51,21.61,483.21,245.25,399.25,343.35]
    # 房屋价格数据
    y = [196.63,203.88,210.75,372.74,202.41,247.61,24.9,239.34,140.32,104.15,176.84,288.23,128.79,49.64,191.74,33.1,30.74,400.02,205.35,330.64,283.45]

    # 计算皮尔逊相关系数，与图形进行比较
    person_house(x, y)

    # 创建画布
    plt.figure(figsize=(20,8),dpi=80)
    # 绘制图像
    plt.scatter(x,y)
    # 显示图像
    plt.show()


    return None

def person_house(x,y):
    r = pearsonr(x, y)
    print("相关性系数：\n", r)

if __name__ == "__main__":
    scatter_house()