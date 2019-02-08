import matplotlib.pyplot as plt

def pie_test():

    # 准备数据
    movie_names =["雷神3：诸神黄昏","正义联盟","东方快车谋杀案","寻梦环游记","全球风暴","降魔传","追捕","七一","大话西游","美人鱼"]
    place_count = [60605,54546,45819,28243,13278,9945,7679,6799,4621,20105]
    # 创建画布
    plt.figure(figsize=(20,8),dpi=80)
    # 绘制饼图
    plt.pie(place_count,labels=movie_names,colors=["b","r","g","y","c","m","y","k","c","b"],autopct="%1.2f%%")
    plt.axis("equal")
    plt.legend()
    # 显示
    plt.show()

    return None

if __name__ == "__main__":
    pie_test()