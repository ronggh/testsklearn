import random
import time
import numpy as np

def ndarray_list():

    # 对1亿个随机数进行求和
    # 使用python原生list
    a = []
    for i in range(100000000):
        a.append(random.random())
    t1 = time.time()
    sum1 = sum(a)
    t2 = time.time()

    # 使用ndarray
    b = np.array(a)
    t3 = time.time()
    sum2 = np.sum(b)
    t4 = time.time()

    print("耗时比较：\n",t2-t1,t4-t3)

    return None

if __name__=="__main__":
    ndarray_list()