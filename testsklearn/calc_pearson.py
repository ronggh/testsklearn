from scipy.stats import pearsonr

def calc_person():
    """
    计算皮尔逊相关系数
    :return:
    """
    x = [12.5,15.3,23.2,26.4,33.5,34.4,39.4,45.2,55.4,60.9]
    y = [21.2,23.9,32.9,34.1,42.5,43.2,49.0,52.8,59.4,63.5]
    r = pearsonr(x,y)
    print("相关性系数：\n",r)

    return  None

if __name__ == "__main__":
    calc_person()