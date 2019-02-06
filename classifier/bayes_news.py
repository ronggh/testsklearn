from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

def bays_news():
    """
    朴素贝叶斯分类——分章分类
    :return:None
    """
    # 获取数据集
    news = fetch_20newsgroups(subset="all")
    # 划分数据集
    x_train,x_test,y_train,y_test = train_test_split(news.data,news.target,test_size=0.25,random_state=22)
    # TFIDF进行特征抽取
    tfv = TfidfVectorizer()
    x_train = tfv.fit_transform(x_train)
    x_test = tfv.transform(x_test)
    # 朴素贝叶斯预测
    estimator = MultinomialNB(alpha=1.0)
    estimator.fit(x_train,y_train)

    # 模型评估
    y_predict = estimator.predict(x_test)
    print("比对真实值与预测值:\n", y_test == y_predict)

    score = estimator.score(x_test,y_test)
    print("准确率为：\n",score)

    return  None

if __name__ == "__main__":
    bays_news()