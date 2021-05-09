import graph
import generators
import time
import measurement
import sys
import random


def generate_worst_graph(n):
    edges = list()
    for i in range(n - 1):
        edges.append((i, i + 1))
    for i in range(n - 1):
        for j in range(i):
            edges.append((i, j))
    return graph.Graph(n, edges, True)


def generate_random_graph(n):
    return graph.Graph(n, generators.generate_connected_graph(n, False), False)


def generate_best_graph(n):
    edges = list()
    for i in range(n):
        for j in range(i):
            edges.append((j, i))
    return graph.Graph(n, edges, False)


def measure_dfs_random():
    f = open("dfs_random.txt", "w")
    for i in range(1, 1000, 2):
        print(i)
        f.write(str(i) + " " + "%.6f" % measurement.test(20, generate_random_graph(i).find_path_dfs,
                                                         random.randint(0, i - 1), random.randint(0, i - 1)) + "\n")
    f.close()


def measure_dfs_worst():
    f = open("dfs_worst.txt", "w")
    for i in range(1, 1000, 2):
        print(i)
        f.write(str(i) + " " + "%.6f" % measurement.test(20, generate_worst_graph(i).find_path_dfs, 0, i - 1) + "\n")
    f.close()


def measure_dfs_best():
    f = open("dfs_best.txt", "w")
    for i in range(2, 1000, 2):
        print(i)
        f.write(str(i) + " " + "%.6f" % measurement.test(20, generate_best_graph(i).find_path_dfs, 0, 1) + "\n")
    f.close()


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    #measure_dfs_best()
    measurement.find_square_approximation("dfs_random.txt")
