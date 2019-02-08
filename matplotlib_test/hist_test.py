import numpy as np
import matplotlib.pyplot as plt

def hist_test():
    """
    hist
    :return:
    """

    np.random.seed(19680801)
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)
    n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)

    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()

    return None

if __name__ == "__main__":
    hist_test()