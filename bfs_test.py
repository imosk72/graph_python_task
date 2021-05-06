import graph
import generators
import time
import measurement
import sys
import random
import dfs_test


def measure_bfs_random():
    f = open("bfs_random.txt", "w")
    for i in range(1, 1000, 2):
        print(i)
        f.write(str(i) + " " + "%.6f" % measurement.test(20, dfs_test.generate_random_graph(i).find_path_bfs,
                                                         random.randint(0, i - 1), random.randint(0, i - 1)) + "\n")
    f.close()


def measure_bfs_worst():
    f = open("bfs_worst.txt", "w")
    for i in range(1, 1000, 2):
        print(i)
        f.write(str(i) + " " + "%.6f" % measurement.test(20, dfs_test.generate_worst_graph(i).find_path_bfs, 0, i - 1) + "\n")
    f.close()


if __name__ == "__main__":
     measurement.find_square_approximation("bfs_worst.txt")
