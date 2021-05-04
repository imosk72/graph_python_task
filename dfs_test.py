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


if __name__ == "__main__":
    # huj(lol)
    for i in range(1, 1000, 100):
        print(measurement.test(20, generate_worst_graph(i).find_path_dfs, 0, i - 1))
