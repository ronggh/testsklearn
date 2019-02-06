import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def kmeans_customer():
    """
    KMeans聚类，客户分类
    :return: None
    """
    # 1、获取数据
    # 原始数据在 https://www.kaggle.com/c/instacart-market-basket-analysis/data
    order_products = pd.read_csv("../data/Instacart/order_products__prior.csv")
    products = pd.read_csv("../data/Instacart/products.csv")
    orders = pd.read_csv("../data/Instacart/orders.csv")
    aisles = pd.read_csv("../data/Instacart/aisles.csv")

    # 2、数据处理-合并表
    table1 = pd.merge(aisles, products, on=["aisle_id", "aisle_id"])
    table2 = pd.merge(table1, order_products, on=["product_id", "product_id"])
    # print(table2.head(10))
    table3 = pd.merge(table2, orders, on=["order_id", "order_id"])
    table = pd.crosstab(table3["user_id"], table3["aisle"])
    # 为运行快，演示时取前1万条
    data = table[:10000]

    # PCA 降维处理,特征太多了
    pca = PCA(n_components=0.95)
    data = pca.fit_transform(data)

    # kMeans 模型
    estimator = KMeans(n_clusters=3)
    estimator.fit(data)
    y_predict = estimator.predict(data)
    print("KMeans预测结果：\n", y_predict)

    # 模型评估-轮廓系数
    score = silhouette_score(data, y_predict)
    print("KMeans评估-轮廓系数;\n", score)

    return None


if __name__ == "__main__":
    kmeans_customer()