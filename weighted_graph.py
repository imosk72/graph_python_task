import queue
import graph


class WeightedGraph:
    def __int__(self):
        self.n = 0
        self.edges = [set()]
        self.has_negative_edge = False

    def __init__(self, n):
        self.n = n
        self.edges = [set() for _ in range(n)]
        self.has_negative_edge = False

    def __init__(self, n, edges, is_oriented):
        self.n = n
        self.edges = [set() for _ in range(n)]
        self.has_negative_edge = False
        for i in edges:
            self.edges[i[0]].add((i[1], i[2]))
            if i[2] < 0:
                self.has_negative_edge = True
            if not is_oriented:
                self.edges[i[1]].add((i[0], i[2]))

    def ford_bellman(self, start, end):
        distances = [float('inf')] * self.n
        ancestor = [-1] * self.n
        ancestor[start] = -2
        distances[start] = 0
        edges = list()
        for i in range(self.n):
            for j in self.edges[i]:
                edges.append((i, j[0], j[1]))

        for i in range(self.n - 1):
            for j in edges:
                if distances[j[0]] < float('inf') and distances[j[1]] > distances[j[0]] + j[2]:
                    distances[j[1]] = distances[j[0]] + j[2]
                    ancestor[j[1]] = j[0]
        in_cycle = list()
        for j in edges:
            if distances[j[0]] < float('inf') and distances[j[1]] > distances[j[0]] + j[2]:
                distances[j[1]] = distances[j[0]] + j[2]
                ancestor[j[1]] = j[0]
                in_cycle.append(j[1])
        if len(in_cycle) == 0:
            return distances[end], graph.restore_path(ancestor, start, end)

        for i in range(len(in_cycle)):
            for j in range(self.n):
                in_cycle[i] = ancestor[in_cycle[i]]
        q = queue.Queue()
        used = [False] * self.n
        for i in in_cycle:
            q.put(i)
            used[i] = True
        while not q.empty():
            v = q.get()
            for to in self.edges[v]:
                if not used[to[0]]:
                    q.put(to[0])
                    used[to[0]] = True
        if used[end]:
            return None
        else:
            return distances[end], graph.restore_path(ancestor, start, end)

    def dijkstra(self, start, end):
        if self.has_negative_edge:
            return None
        distance = [float('inf')] * self.n
        ancestor = [-1] * self.n
        ancestor[start] = -2
        distance[start] = 0
        q = queue.PriorityQueue()
        q.put((0, start))

        while not q.empty():
            dist, v = q.get()
            if dist > distance[v]:
                continue
            if v == end:
                break
            for to in self.edges[v]:
                if distance[to[0]] > distance[v] + to[1]:
                    distance[to[0]] = distance[v] + to[1]
                    ancestor[to[0]] = v
                    q.put((distance[to[0]], to[0]))

        return distance[end], graph.restore_path(ancestor, start, end)

    def floyd(self):
        ans = [[float('inf')] * self.n] * self.n
        for i in range(self.n):
            ans[i][i] = 0
            for j in self.edges[i]:
                ans[i][j[0]] = j[1]
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if ans[i][k] != float('inf') and ans[k][i] != float('inf') and ans[i][j] > ans[i][k] + ans[k][j]:
                        ans[i][j] = ans[i][k] + ans[k][j]
        return ans




