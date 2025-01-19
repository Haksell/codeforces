# ruff: noqa: E731, E741
from collections import defaultdict
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


class UnionFind:
    def __init__(self, n=0):
        self.__len = self.__num_components = n
        self.__parents = list(range(n))
        self.__ranks = [1] * n

    def __len__(self):
        return self.__len

    @property
    def num_components(self):
        return self.__num_components

    def __repr__(self):
        components = (
            str(list(self)).replace(",", "").replace("[", "{").replace("]", "}")
        )[1:-1]
        return f"{self.__class__.__name__}({components})"

    def __iter__(self):
        components = defaultdict(list)
        for i in range(self.__len):
            components[self.find(i)].append(i)
        yield from components.values()

    def find(self, u):
        while u != self.__parents[u]:
            self.__parents[u] = self.__parents[self.__parents[u]]
            u = self.__parents[u]
        return u

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return
        self.__num_components -= 1
        if self.__ranks[root_u] > self.__ranks[root_v]:
            self.__parents[root_v] = root_u
        else:
            self.__parents[root_u] = root_v
            self.__ranks[root_v] += self.__ranks[root_v] == self.__ranks[root_u]

    def connected(self, u, v):
        return self.find(u) == self.find(v)

    def add(self):
        n = self.__len
        self.__parents.append(n)
        self.__ranks.append(1)
        self.__len += 1
        self.__num_components += 1
        return n


def parse_graph(n, m):
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = mir()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    return g


def solve():
    n, mf, mg = mir()
    edges_f = [tuple(x - 1 for x in mir()) for _ in range(mf)]
    edges_g = [tuple(x - 1 for x in mir()) for _ in range(mg)]
    uf_g = UnionFind(n)
    for u, v in edges_g:
        uf_g.union(u, v)
    r = 0
    uf_f = UnionFind(n)
    for u, v in edges_f:
        if uf_g.connected(u, v):
            uf_f.union(u, v)
        else:
            r += 1
    r += uf_f.num_components - uf_g.num_components
    print(r)


def main():
    for _ in rir():
        solve()


def test():
    pass


if __name__ == "__main__":
    if sys.stdin.isatty():
        test()
    else:
        main()
