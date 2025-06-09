# ruff: noqa: E731, E741
from collections import defaultdict
import math
from operator import itemgetter
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
        self.__min_w = [math.inf] * n

    def __len__(self):
        return self.__len

    @property
    def num_components(self):
        return self.__num_components

    def min_w(self, u):
        root = self.find(u)
        return self.__min_w[root]

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

    def union(self, u, v, w):
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return
        self.__num_components -= 1
        if self.__ranks[root_u] > self.__ranks[root_v]:
            self.__parents[root_v] = root_u
        else:
            self.__parents[root_u] = root_v
            self.__ranks[root_v] += self.__ranks[root_v] == self.__ranks[root_u]
        self.__min_w[root_u] = self.__min_w[root_v] = min(
            w, self.__min_w[root_u], self.__min_w[root_v]
        )

    def connected(self, u, v):
        return self.find(u) == self.find(v)

    def add(self):
        n = self.__len
        self.__parents.append(n)
        self.__ranks.append(1)
        self.__len += 1
        self.__num_components += 1
        return n


def solve():
    n, m = mir()
    edges = []
    for _ in range(m):
        u, v, w = mir()
        edges.append((u - 1, v - 1, w))

    uf = UnionFind(n)
    res = math.inf
    for u, v, w in sorted(edges, key=itemgetter(2)):
        uf.union(u, v, w)
        if uf.connected(0, n - 1):
            res = min(res, w + uf.min_w(0))
    print(res)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
