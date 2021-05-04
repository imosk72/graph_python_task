import queue
import random


def restore_path(ancestor, start, end):
    if ancestor[end] == -1:
        return None
    ans = list()
    while end != start:
        ans.append(end)
        end = ancestor[end]
    ans.append(start)
    ans.reverse()
    return ans


class Graph:
    def __int__(self):
        self.n = 0
        self.edges = []

    def __init__(self, n):
        self.n = n
        self.edges = [set() for _ in range(n)]

    def __init__(self, n, edges, is_oriented):
        self.n = n
        self.edges = [set() for _ in range(n)]
        for i in edges:
            self.edges[i[0]].add(i[1])
            if not is_oriented:
                self.edges[i[1]].add(i[0])

    def find_path_bfs(self, start, end):
        ancestor = [-1] * self.n
        ancestor[start] = -2
        q = queue.Queue()
        q.put(start)
        while not q.empty():
            v = q.get()
            if v == end:
                return restore_path(ancestor, start, end)

            for to in self.edges[v]:
                if ancestor[to] == -1:
                    ancestor[to] = v
                    q.put(to)
        return None

    def dfs(self, ancestor, v, start, end):
        if v == end:
            return True
        for to in self.edges[v]:
            if ancestor[to] == -1:
                ancestor[to] = v
                if self.dfs(ancestor, to, start, end):
                    return True
        return False

    def find_path_dfs(self, start, end):
        ancestor = [-1] * self.n
        ancestor[start] = -2
        self.dfs(ancestor, start, start, end)
        return restore_path(ancestor, start, end)
