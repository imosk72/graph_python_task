import queue
import copy
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

    def find_hamilton_cycle(self):
        if self.n == 1:
            return [0]
        ancestor = [[-1] * self.n for i in range(1 << self.n)]
        ancestor[1 << 0][0] = -2
        for i in range(1 << self.n):
            for j in range(self.n):
                if ((1 << j) & i) == 0 or ancestor[i][j] == -1:
                    continue
                for k in self.edges[j]:
                    if ((1 << k) & i) == 0:
                        ancestor[(1 << k) | i][k] = j

        for i in range(self.n):
            if ancestor[(1 << self.n) - 1][i] >= 0 and 0 in self.edges[i]:
                ans = []
                pos = i
                mask = (1 << self.n) - 1
                while pos != 0:
                    ans.append(pos)
                    cur = pos
                    pos = ancestor[mask][pos]
                    mask -= (1 << cur)

                ans.append(0)
                ans.reverse()
                return ans
        return None

    def find_euler_cycle(self):
        in_deg = [0] * self.n
        for i in range(self.n):
            for to in self.edges[i]:
                in_deg[to] += 1
        for i in range(self.n):
            if len(self.edges[i]) != in_deg[i]:
                return None

        edges = copy.deepcopy(self.edges)
        st = []
        ans = []
        st.append(0)
        while len(st) != 0:
            v = st[-1]
            if len(edges[v]) == 0:
                ans.append(v)
                st.pop()
            else:
                st.append(edges[v].pop())
        ans.reverse()
        return ans



