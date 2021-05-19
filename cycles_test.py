import graph
import measurement
import generators
import dfs_test


def measure_hamilton_cycle_best():
    f = open("hamilton_cycle_best.txt", "w")
    for i in range(1, 21):
        print(i)
        f.write(str(i) + " " + "%.6f" % measurement.test(20, graph.Graph(i, generators.generate_chain(i, False), False).find_hamilton_cycle) + "\n")
    f.close()


def measure_hamilton_cycle_worst():
    f = open("hamilton_cycle_worst.txt", "w")
    for i in range(1, 21):
        print(i)
        f.write(str(i) + " " + "%.6f" % measurement.test(20, dfs_test.generate_worst_graph(i).find_hamilton_cycle) + "\n")
    f.close()


def measure_euler_cycle_best():
    f = open("euler_cycle_best.txt", "w")
    for i in range(1, 1000, 2):
        print(i)
        f.write(str(i) + " " + "%.6f" % measurement.test(20, graph.Graph(i, generators.generate_chain(i, False), False).find_euler_cycle) + "\n")
    f.close()


def measure_euler_cycle_worst():
    f = open("euler_cycle_worst.txt", "w")
    for i in range(1, 500, 2):
        print(i)
        f.write(str(i) + " " + "%.6f" % measurement.test(20, dfs_test.generate_worst_graph(i).find_euler_cycle) + "\n")
    f.close()


if __name__ == "__main__":
    #measure_euler_cycle_worst()
    measurement.find_exponential("hamilton_cycle_worst.txt")