import weighted_graph
import random
import measurement
import generators
import dijkstra_test


def generate_worst_graph(n):
    edges = list()
    for i in range(n):
        for j in range(i):
            edges.append((j, i, random.randint(-10000000, 10000000)))
    return weighted_graph.WeightedGraph(n, edges, False)


def measure_tree():
    f = open("ford_bellman_tree.txt", "w")
    for i in range(2, 200, 2):
        print(i)
        f.write(str(i) + " " + "%.6f" % measurement.test(20, weighted_graph.WeightedGraph(i, generators.generate_tree(i, True, True), False).ford_bellman, random.randint(0, i - 1), random.randint(0, i - 1)) + "\n")
    f.close()


def measure_random():
    f = open("ford_bellman_random.txt", "w")
    for i in range(2, 100, 2):
        print(i)
        f.write(str(i) + " " + "%.6f" % measurement.test(20, weighted_graph.WeightedGraph(i, generators.generate_connected_graph(i, True, True),False).ford_bellman, random.randint(0, i - 1), random.randint(0, i - 1)) + "\n")
    f.close()


def measure_worst():
    f = open("ford_bellman_worst.txt", "w")
    for i in range(2, 100, 2):
        print(i)
        f.write(str(i) + " " + "%.6f" % measurement.test(20, dijkstra_test.generate_worst_graph(i).ford_bellman, 0, i - 1) + "\n")
    f.close()


if __name__ == "__main__":
    #measure_random()
    measurement.compare_charts("ford_bellman_worst.txt", "dijkstra_worst.txt")
