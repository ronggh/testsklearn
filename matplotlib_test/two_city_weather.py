# 显示两个城市11点到12点1小时内每分钟的温度变化折线图，
# 一个温度范围在15~18度；另一个在1到3度之间
import matplotlib.pyplot as plt
import random

def two_city_weather():

    # 准备数据
    x = range(60)
    y_shanghai = [random.uniform(15,18) for i in x]
    y_beijing =  [random.uniform(1,3) for i in x]
    # 创建画布
    plt.figure(figsize=(20,8),dpi=80)
    # 绘制图像
    plt.plot(x,y_shanghai,color='r',linestyle='-.',linewidth=0.5,label="上海")
    plt.plot(x,y_beijing,color='b',linestyle='--',linewidth=0.3,label="北京")
    # 显示图例
    plt.legend(loc="best")
    # 设置坐标轴刻度,x轴刻度每隔5分钟；y轴刻度从0到40，每隔5度显示一个刻度
    # 准备X的刻度说明
    x_label = ["11点{}分".format(i) for i in x]
    plt.xticks(x[::5],x_label[::5])
    plt.yticks(range(0,40,5))
    # 添加网格显示
    plt.grid(True,linestyle='--',alpha=0.5)
    # 添加标题和坐标轴描述信息
    plt.title("北京、上海中午11:00到12:00温度变化曲线")
    plt.xlabel("时间")
    plt.ylabel("温度")
    # 显示图像
    plt.show()

    return None

if __name__ == "__main__":
    two_city_weather()