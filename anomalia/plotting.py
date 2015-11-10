import matplotlib.pyplot as plt
import numpy as np


def simple(data, xlabel, ylabel):
    t = np.arange(0.0, 2.0, 0.01)
    plt.plot(t, data)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title('Anomaly detection')
    plt.grid(True)
    #plt.savefig("test.png")
    plt.show()

