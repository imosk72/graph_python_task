from matplotlib import pyplot as plt
import numpy as np
import time


def test(count, func, *args, **kwargs):
    ans = func(*args, **kwargs)
    ans = func(*args, **kwargs)
    sum = 0
    for i in range(count):
        t = time.perf_counter()
        ans = func(*args, **kwargs)
        sum += time.perf_counter() - t
    return sum / count


def read_data(name):
    f = open(name, "r")
    x, y = [], []
    for line in f:
        x.append(int(line.split()[0]))
        y.append(float(line.split()[1]))
    return x, y


def find_square_approximation(name):
    x, y = read_data(name)
    A = np.zeros(shape=[len(x), 3])
    b = np.zeros(shape=[len(x)])
    for i in range(len(x)):
        A[i][0] = x[i]**2
        A[i][1] = x[i]
        A[i][2] = 1
        b[i] = y[i]
    answer = np.linalg.solve(np.dot(A.T, A), np.dot(A.T, b))
    print("%.10f %.10f %.10f" % (answer[0], answer[1], answer[2]))
    y1 = [answer[0] * x[i]**2 + answer[1] * x[i] + answer[2] for i in range(len(x))]
    plt.plot(x, y, "ro", x, y1)
    plt.show()


def find_linear_approximation(name):
    x, y = read_data(name)
    A = np.zeros(shape=[len(x), 2])
    b = np.zeros(shape=[len(x)])
    for i in range(len(x)):
        A[i][0] = x[i]
        A[i][1] = 1
        b[i] = y[i]
    answer = np.linalg.solve(np.dot(A.T, A), np.dot(A.T, b))
    print("%.10f %.10f" % (answer[0], answer[1]))
    y1 = [answer[0] * x[i] + answer[1] for i in range(len(x))]
    plt.plot(x, y, "ro", x, y1)
    plt.show()
