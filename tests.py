import unittest
import graph
import weighted_graph
import generators
import random
import queue
import sys


class MyTestCase(unittest.TestCase):
    def is_connected(self, n, edges):
        g = [[] for _ in range(n)]
        for i in edges:
            g[i[0]].append(i[1])
            g[i[1]].append(i[0])
        q = queue.Queue()
        used = [1] + [0] * (n - 1)
        q.put(0)
        while not q.empty():
            v = q.get()
            for to in g[v]:
                if used[to] == 0:
                    q.put(to)
                    used[to] = 1
        for i in used:
            if i != 1:
                return False
        return True

    def test_simple_undirected_graph(self):
        g = graph.Graph(5, {(0, 1), (1, 2), (4, 3), (2, 3)}, False)
        path_dfs = g.find_path_dfs(0, 4)
        path_bfs = g.find_path_bfs(0, 4)
        self.assertEqual(path_dfs, [0, 1, 2, 3, 4])
        self.assertEqual(path_bfs, [0, 1, 2, 3, 4])

    def test_simple_directed_graph(self):
        g = graph.Graph(5, {(0, 1), (1, 2), (4, 3), (2, 3)}, True)
        path_dfs = g.find_path_dfs(0, 4)
        path_bfs = g.find_path_bfs(0, 4)
        self.assertEqual(path_dfs, None)
        self.assertEqual(path_bfs, None)

    def test_tree_generator(self):
        for i in range(50):
            n = random.randint(1, i * 500 + 228)
            tree = generators.generate_tree(n, False)
            self.assertEqual(len(tree), n - 1)
            self.assertEqual(self.is_connected(n, tree), True)

    def test_connected_graph_generator(self):
        for i in range(50):
            n = random.randint(1, i * 50 + 228)
            g = generators.generate_connected_graph(n, False)
            self.assertEqual(self.is_connected(n, g), True)

    def test_connected_undirected_graph(self):
        sys.setrecursionlimit(10000)
        for i in range(20):
            n = random.randint(1, 1000)
            edges = generators.generate_connected_graph(n, False)
            g = graph.Graph(n, edges, False)
            for j in range(50):
                start = random.randint(0, n - 1)
                end = random.randint(0, n - 1)
                path_dfs = g.find_path_dfs(start, end)
                path_bfs = g.find_path_bfs(start, end)
                self.assertFalse(path_bfs is None)
                self.assertFalse(path_dfs is None)
                self.assertTrue(path_bfs[0] == start)
                self.assertTrue(path_bfs[-1] == end)
                self.assertTrue(path_dfs[0] == start)
                self.assertTrue(path_dfs[-1] == end)
                for k in range(len(path_bfs) - 1):
                    self.assertTrue(((path_bfs[k], path_bfs[k + 1]) in edges) or ((path_bfs[k + 1], path_bfs[k]) in edges))
                for k in range(len(path_dfs) - 1):
                    self.assertTrue(((path_dfs[k], path_dfs[k + 1]) in edges) or ((path_dfs[k + 1], path_dfs[k]) in edges))

    def test_undirected_graph(self):
        sys.setrecursionlimit(10000)
        for i in range(20):
            n = random.randint(1, 1000)
            edges = generators.generate_graph(n, False)
            g = graph.Graph(n, edges, False)
            color = [-1] * n
            all = 0
            for i in range(n):
                if color[i] == -1:
                    q = queue.Queue()
                    q.put(i)
                    color[i] = all
                    while not q.empty():
                        v = q.get()
                        for to in g.edges[v]:
                            if color[to] == -1:
                                q.put(to)
                                color[to] = all
                    all += 1

            for j in range(50):
                start = random.randint(0, n - 1)
                end = random.randint(0, n - 1)
                path_dfs = g.find_path_dfs(start, end)
                path_bfs = g.find_path_bfs(start, end)
                if color[start] != color[end]:
                    self.assertTrue(path_bfs is None)
                    self.assertTrue(path_dfs is None)
                else:
                    self.assertTrue(path_bfs[0] == start)
                    self.assertTrue(path_bfs[-1] == end)
                    self.assertTrue(path_dfs[0] == start)
                    self.assertTrue(path_dfs[-1] == end)
                    for k in range(len(path_bfs) - 1):
                        self.assertTrue(
                            ((path_bfs[k], path_bfs[k + 1]) in edges) or ((path_bfs[k + 1], path_bfs[k]) in edges))
                    for k in range(len(path_dfs) - 1):
                        self.assertTrue(
                            ((path_dfs[k], path_dfs[k + 1]) in edges) or ((path_dfs[k + 1], path_dfs[k]) in edges))

    def test_directed_graph(self):
        sys.setrecursionlimit(10000)
        for i in range(10):
            n = random.randint(1, 100)
            edges = generators.generate_graph(n, False)
            g = graph.Graph(n, edges, True)
            for j in range(10):
                start = random.randint(0, n - 1)
                possible = {start}
                impossible = {i for i in range(n)}
                impossible.remove(start)
                q = queue.Queue()
                q.put(start)
                while not q.empty():
                    v = q.get()
                    for to in g.edges[v]:
                        if to not in possible:
                            q.put(to)
                            possible.add(to)
                            impossible.remove(to)
                count = 0
                for k in impossible:
                    if count >= 10:
                        break
                    path_dfs = g.find_path_dfs(start, k)
                    path_bfs = g.find_path_bfs(start, k)
                    self.assertTrue(path_bfs is None)
                    self.assertTrue(path_dfs is None)
                    count += 1

                count = 0
                for k in possible:
                    if count >= 10:
                        break
                    path_dfs = g.find_path_dfs(start, k)
                    path_bfs = g.find_path_bfs(start, k)
                    self.assertTrue(path_bfs[0] == start)
                    self.assertTrue(path_bfs[-1] == k)
                    self.assertTrue(path_dfs[0] == start)
                    self.assertTrue(path_dfs[-1] == k)
                    for l in range(len(path_bfs) - 1):
                        self.assertTrue((path_bfs[l], path_bfs[l + 1]) in edges)
                    for l in range(len(path_dfs) - 1):
                        self.assertTrue((path_dfs[l], path_dfs[l + 1]) in edges)

    def test_shortest_path1(self):
        g = weighted_graph.WeightedGraph(3, [(0, 1, 3), (0, 2, 1), (2, 1, 1)], True)
        self.assertEqual(g.dijkstra(0, 1), (2, [0, 2, 1]))
        self.assertEqual(g.ford_bellman(0, 1), (2, [0, 2, 1]))

    def test_shortest_path2(self):
        g = weighted_graph.WeightedGraph(2, [(0, 1, -2), (1, 0, 1)], True)
        self.assertEqual(g.dijkstra(0, 1), None)
        self.assertEqual(g.ford_bellman(0, 1), None)

    def test_shortest_path3(self):
        g = weighted_graph.WeightedGraph(4, [(0, 1, -2), (0, 2, 1), (2, 3, -1), (3, 2, -1)], True)
        self.assertEqual(g.dijkstra(0, 1), None)
        self.assertEqual(g.ford_bellman(0, 1), (-2, [0, 1]))
        self.assertEqual(g.ford_bellman(0, 2), None)

    def test_shortest_path4(self):
        g = weighted_graph.WeightedGraph(4, [(0, 1, 1), (0, 2, 100000000), (2, 1, 1000000000), (2, 3, -1), (3, 2, -1)], True)
        self.assertEqual(g.dijkstra(0, 1), None)
        self.assertEqual(g.ford_bellman(0, 2), None)

    def test_shortest_path5(self):
        g1 = weighted_graph.WeightedGraph(2, [(0, 1, 228), (1, 0, 1)], True)
        self.assertEqual(g1.dijkstra(0, 1), (228, [0, 1]))
        self.assertEqual(g1.ford_bellman(0, 1), (228, [0, 1]))
        g2 = weighted_graph.WeightedGraph(2, [(0, 1, 228), (1, 0, 1)], False)
        self.assertEqual(g2.dijkstra(0, 1), (1, [0, 1]))
        self.assertEqual(g2.ford_bellman(0, 1), (1, [0, 1]))
        g3 = weighted_graph.WeightedGraph(2, [(0, 1, 228), (1, 0, -1)], False)
        self.assertEqual(g3.dijkstra(0, 1), None)
        self.assertEqual(g3.ford_bellman(0, 1), None)
        g4 = weighted_graph.WeightedGraph(2, [(0, 1, 228), (1, 0, -1)], True)
        self.assertEqual(g4.dijkstra(0, 1), None)
        self.assertEqual(g4.ford_bellman(0, 1), (228, [0, 1]))


if __name__ == '__main__':
    unittest.main()
