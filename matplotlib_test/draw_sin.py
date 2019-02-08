import numpy as np
import matplotlib.pyplot as plt

def draw_sin():
    """
    draw sin() function
    :return:
    """
    # 准备数据
    x = np.linspace(-10,10,1000)
    # 计算sin
    y = np.sin(x)

    # 准备画布
    plt.figure(figsize=(20,8),dpi=100)
    # 绘制图像
    plt.plot(x,y)
    plt.grid()

    # 显示图像
    plt.show()

    return None

if __name__ == "__main__":
    draw_sin()
