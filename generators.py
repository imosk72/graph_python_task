import random


def generate_chain(n, is_weighted, has_negative_edges = False):
    ans = set()
    for i in range(n - 1):
        if is_weighted:
            if has_negative_edges:
                ans.add((i, i + 1, random.randint(-1000000000, 1000000000)))
            else:
                ans.add((i, i + 1, random.randint(0, 1000000000)))
        else:
            ans.add((i, i + 1))
    return ans


def generate_tree(n, is_weighted, has_negative_edges = False):
    ans = set()
    order = [i for i in range(n)]
    random.shuffle(order)
    for i in range(1, n):
        if is_weighted:
            if has_negative_edges:
                ans.add((order[i], order[random.randint(0, i - 1)], random.randint(-1000000000, 1000000000)))
            else:
                ans.add((order[i], order[random.randint(0, i - 1)], random.randint(0, 1000000000)))
        else:
            ans.add((order[i], order[random.randint(0, i - 1)]))
    return ans


def generate_connected_graph(n, is_weighted, has_negative_edges = False):
    ans = generate_tree(n, is_weighted, has_negative_edges)
    for i in range(random.randint(0, min(100500, n * (n - 1) // 2))):
        if is_weighted:
            if has_negative_edges:
                ans.add((random.randint(0, n - 1), random.randint(0, n - 1), random.randint(-1000000000, 1000000000)))
            else:
                ans.add((random.randint(0, n - 1), random.randint(0, n - 1), random.randint(0, 1000000000)))
        else:
            ans.add((random.randint(0, n - 1), random.randint(0, n - 1)))
    return ans


def generate_graph(n, is_weighted, has_negative_edges = False):
    ans = set()
    for i in range(random.randint(0, min(100500, n * (n - 1) // 2))):
        if is_weighted:
            if has_negative_edges:
                ans.add((random.randint(0, n - 1), random.randint(0, n - 1), random.randint(-1000000000, 1000000000)))
            else:
                ans.add((random.randint(0, n - 1), random.randint(0, n - 1), random.randint(0, 1000000000)))
        else:
            ans.add((random.randint(0, n - 1), random.randint(0, n - 1)))
    return ans
