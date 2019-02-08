import matplotlib.pyplot as plt

def bar_movie1():
    """
    显示电影排行
    :return:
    """
    # 1、准备数据
    movie_names =["雷神3：诸神黄昏","正义联盟","东方快车谋杀案","寻梦环游记","全球风暴","降魔传","追捕","七一","大话西游","美人鱼"]
    tickets = [73853,57767,22354,15969,14839,8725,8316,7916,6764,52222]
    # 创建画布
    plt.figure(figsize=(20,8),dpi=80)
    # 绘制柱状图
    x_ticks = range(len(movie_names))
    plt.bar(x_ticks,tickets,color=["b","r","g","y","c","m","y","k","c","b"])
    # 修改X刻度
    plt.xticks(x_ticks,movie_names)
    # 添加标题和网格
    plt.title("电影票房收入对比")
    plt.grid(linestyle="--",alpha=0.5)
    # 显示图像
    plt.show()

    return  None

def bar_movie2():
    # 1、准备数据
    movie_names = ["雷神3：诸神黄昏", "正义联盟", "寻梦环游记"]
    first_day = [10587.6, 10062.5, 1275.7]
    first_weekend = [36224.9, 34479.6, 11830]
    # 创建画布
    plt.figure(figsize=(20, 8), dpi=80)
    # 绘制柱状图
    x = range(3)
    plt.bar(x, first_day, width=0.2, label="首日票房")
    plt.bar([i + 0.2 for i in x], first_weekend, width=0.2, label="首周票房")
    # 修改刻度
    plt.xticks([i + 0.1 for i in x], movie_names)
    plt.legend(loc="best")

    # 显示图像
    plt.show()
    return None

if __name__ == "__main__":
    # bar_movie1()
    bar_movie2()