import weighted_graph
import measurement
import generators


def generate_best_graph(n):
    edges = list()
    for i in range(n):
        for j in range(i):
            if j == 0 and i == 1:
                edges.append((j, i, 1))
            else:
                edges.append((j, i, 2))
    return weighted_graph.WeightedGraph(n, edges, False)


def generate_worst_graph(n):
    edges = list()
    for i in range(n - 1):
        edges.append((i, i + 1, 0))
        for j in range(i + 1, n):
            edges.append((i, j, n - i))
    return weighted_graph.WeightedGraph(n, edges, False)


def measure_dijkstra_best():
    f = open("dijkstra_best.txt", "w")
    for i in range(2, 1000, 2):
        print(i)
        f.write(str(i) + " " + "%.6f" % measurement.test(20, generate_best_graph(i).dijkstra, 0, 1) + "\n")
    f.close()


def measure_dijkstra_worst():
    f = open("dijkstra_worst.txt", "w")
    for i in range(1, 300, 2):
        print(i)
        f.write(str(i) + " " + "%.6f" % measurement.test(20, generate_worst_graph(i).dijkstra, 0, i - 1) + "\n")
    f.close()


def measure_dijkstra_random():
    f = open("dijkstra_random.txt", "w")
    for i in range(1, 500, 2):  
        print(i)
        f.write(str(i) + " " + "%.6f" % measurement.test(20, weighted_graph.WeightedGraph(i, generators.generate_connected_graph(i, True), False).dijkstra, 0, i - 1) + "\n")
    f.close()


if __name__ == "__main__":
    #measure_dijkstra_best()
    measurement.build_chart("dijkstra_random.txt")
