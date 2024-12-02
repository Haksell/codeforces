# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


class UnionFind:
    def __init__(self, n):
        self.__len = n
        self.__parents = list(range(n))
        self.__ranks = [1] * n

    def __len__(self):
        return self.__len

    def find(self, u):
        while u != self.__parents[u]:
            self.__parents[u] = self.__parents[self.__parents[u]]
            u = self.__parents[u]
        return u

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return True
        if self.__ranks[root_u] > self.__ranks[root_v]:
            self.__parents[root_v] = root_u
        elif self.__ranks[root_v] > self.__ranks[root_u]:
            self.__parents[root_u] = root_v
        else:
            self.__parents[root_u] = root_v
            self.__ranks[root_v] += 1
        return False

    def num_components(self):
        return len({self.find(i) for i in range(self.__len)})


def main():
    n = ir()
    uf = UnionFind(n)
    points = []
    for i in range(n):
        x1, y1 = mir()
        for j, (x2, y2) in enumerate(points):
            if x1 == x2 or y1 == y2:
                uf.union(i, j)
        points.append((x1, y1))
    print(uf.num_components() - 1)


if __name__ == "__main__":
    main()
