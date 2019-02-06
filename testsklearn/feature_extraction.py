# 特征抽取
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler,StandardScaler,Imputer
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA

import jieba

def dictvec():
    """
    字典数据抽取
    :return:None
    """
    # 实例化DictVectorizer,默认输出结果为sparse矩阵
    # dict = DictVectorizer(sparse=False)
    dict = DictVectorizer()
    # 调用fit_transform
    data = dict.fit_transform([{"city":"北京","temperature":100},{"city":"上海","temperature":60},{"city":"深圳","temperature":30}])
    print(dict.get_feature_names())
    print(data)
    return None

def textvect():
    """
    文本特征化抽取
    :return: None
    """
    # 实例化CountVectorizer
    vector = CountVectorizer()
    # 调用fit_transform输入并转换数据
    # 以两个短句子为例
    res = vector.fit_transform(["life is short,I like python", "Life is too long, I dislike python"])

    # 打印结果
    print(vector.get_feature_names())
    print(res.toarray())

    return  None

def cutword():
    """
    中文分词
    :return:
    """
    # 切词
    con1 = jieba.cut("今天很残酷，明天更残酷，但是后天很美好，但是大多数人死在了明天的晚上")
    con2 = jieba.cut("越是肤浅的越得意忘形，自命不凡；越是深厚的越诚信笃行，保持低调。")
    con3 = jieba.cut("遇见的人，经历的事，都有它存在的意义。")

    # 转换成列表
    content1 = list(con1)
    content2 = list(con2)
    content3 = list(con3)

    # 转成空隔分割的字符串
    c1 = " ".join(content1)
    c2 = " ".join(content2)
    c3  = " ".join(content3)

    return c1,c2,c3

def hanzivec():
    """
    中文文本特征化
    :return:None
    """
    c1,c2,c3 = cutword()
    print(c1,c2,c3)
    cv = CountVectorizer()
    data = cv.fit_transform([c1,c2,c3])
    print(cv.get_feature_names())
    print(data.toarray())

    return None

def tfidfvec():
    """
    中文文本特征化
    :return:None
    """
    c1,c2,c3 = cutword()
    print(c1,c2,c3)
    tf = TfidfVectorizer()
    data = tf.fit_transform([c1,c2,c3])
    print(tf.get_feature_names())
    print(data.toarray())

    return None

def minmax():
    """
    归一化处理
    :return:None
    """
    # mm = MinMaxScaler()，默认[0,1],可以指定想要的范围
    mm = MinMaxScaler(feature_range=(1,10))
    data = mm.fit_transform([[90,2,10,40],[60,4,15,45],[75,3,13,46]])
    print(data)

    return None

def standscaler():
    """
    标准化缩放
    :return: None
    """
    ss = StandardScaler();
    data = ss.fit_transform([[1.,-1.,3.],[2.,4.,2.],[4.,6.,-1.]])
    print(data)

    return None

def im():
    """
    缺失值处理
    :return: None
    """
    # NaN,nan
    im = Imputer(missing_values='NaN', strategy='mean', axis=0)
    data = im.fit_transform([[1, 2], [np.nan, 3], [7, 6]])
    print(data)

    return None

def variance():
    """
    特征过滤——删除低方差特征
    :return: None
    """
    var = VarianceThreshold(threshold=0.0)
    data = var.fit_transform([[0,2,0,3],[0,1,4,3],[0,1,1,3]])
    print(data)

    return None

def pca():
    """
    主成分分析进行特征降维
    :return: None
    """
    pca = PCA(n_components=0.90)
    data = pca.fit_transform([[2,8,4,5],[6,3,0,8],[5,4,9,1]])
    print(data)

    return None

if __name__ =="__main__":
    # dictvec()
    # textvect()
    # hanzivec()
    # tfidfvec()
    # minmax()
    # standscaler()
    # im()
    # variance()
    pca()