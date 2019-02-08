import matplotlib.pyplot as plt
import random

def plt_1():
    '''
    matplotlib 示例1
    :return:
    '''
    plt.figure()
    plt.plot([1,0,9],[4,5,6])
    plt.show()

    return None

def week_weather_sh_plot():
    """
    上海一周天气的折线图
    :return:
    """
    # 创建画布(容器层)
    plt.figure()
    # 绘制折线图(图像层)
    plt.plot([1, 2, 3, 4, 5, 6, 7], [17, 17, 18, 15, 11, 11, 13])
    # 显示图像
    plt.show()

    return None

def time_weather_sh():
    """
    显示某城市11点到12点1小时内每分钟的温度变化折线图，温度范围在15~18度。
    :return:
    """
    # 准备数据
    x = range(60)
    y_shanghai = [random.uniform(15, 18) for i in x]
    # 创建画布
    plt.figure(figsize=(20, 8), dpi=80)
    # 绘制图像
    plt.plot(x, y_shanghai)
    # 设置坐标轴刻度,x轴刻度每隔5分钟；y轴刻度从0到40，每隔5度显示一个刻度
    # 准备X的刻度说明
    x_label = ["11点{}分".format(i) for i in x]
    plt.xticks(x[::5], x_label[::5])
    plt.yticks(range(0, 40, 5))
    # 添加网格显示
    plt.grid(True, linestyle='--', alpha=0.5)
    # 添加标题和坐标轴描述信息
    plt.title("中午11:00到12:00温度变化曲线")
    plt.xlabel("时间")
    plt.ylabel("温度")
    # 显示图像
    plt.show()

    return None

if __name__ == "__main__":
    #plt_1()
    # 上海一周天气的折线图
    # week_weather_sh_plot()
    # 显示某城市11点到12点1小时内每分钟的温度变化折线图，温度范围在15~18度。
    time_weather_sh()
    