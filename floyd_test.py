import generators
import measurement
import weighted_graph


def measure_floyd():
    f = open("floyd.txt", "w")
    for i in range(1, 100):
        print(i)
        f.write(str(i) + " " + "%.6f" % measurement.test(20, weighted_graph.WeightedGraph(i, generators.generate_graph(i, True, True), True).floyd) + "\n")
    f.close()


if __name__ == "__main__":
    #measure_floyd()
    measurement.find_cubic_approximation("floyd.txt")
