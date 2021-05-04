import graph
import weighted_graph
import generators
import time
from matplotlib import pyplot as plt


def measure_time(func):
    def measure(*args, **kwargs):
        t = time.perf_counter()
        res = func(*args, **kwargs)
        print("for func", func.__name__, "time is %.5f" % (time.perf_counter() - t))
        return res

    return measure


def test_dfs(huj):
    t = time.perf_counter()
    ans = huj.find_path_dfs(0, huj.n - 1)
    return time.perf_counter() - t


def test_bfs(huj):
    t = time.perf_counter()
    ans = huj.find_path_bfs(0, huj.n - 1)
    return time.perf_counter() - t


def test_floyd(huj):
    t = time.perf_counter()
    ans = huj.floyd()
    return time.perf_counter() - t


def gen(n):
    return weighted_graph.WeightedGraph(n, generators.generate_chain(n, True), False)


if __name__ == "__main__":
    x, y = [], []
    x1 = [i for i in range(1, 602)]
    y1 = [i**3/3000000 for i in range(1, 602)]
    for i in range(1, 602, 100):
        print(i)
        x.append(i)
        g = gen(i)
        y.append(test_floyd(g))
    plt.plot(x, y, x1, y1)
    plt.show()