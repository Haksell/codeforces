# ruff: noqa: E731, E741
from bisect import bisect_right
from random import choices, randint, seed
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


class UnionFind:
    def __init__(self, n, a, divs):
        self.__len = self.__num_components = n
        self.__parents = list(range(n))
        self.__ranks = [1] * n
        self.__sizes = [1] * n
        self.__divs = [set() for _ in range(n)]
        w = len(a[0])
        for y, row in enumerate(a):
            for x, ai in enumerate(row):
                if ai in divs:
                    self.__divs[y * w + x].add(ai)

    def __len__(self):
        return self.__len

    def find(self, u):
        while u != self.__parents[u]:
            self.__parents[u] = self.__parents[self.__parents[u]]
            u = self.__parents[u]
        return u

    def union(self, u, v, target_size, div):
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return
        self.__num_components -= 1
        if self.__ranks[root_u] > self.__ranks[root_v]:
            root_u, root_v = root_v, root_u
        self.__parents[root_u] = root_v
        self.__ranks[root_v] += self.__ranks[root_v] == self.__ranks[root_u]
        self.__sizes[root_v] += self.__sizes[root_u]

        if len(self.__divs[root_v]) >= len(self.__divs[root_u]):
            self.__divs[root_v] |= self.__divs[root_u]
            self.__divs[root_u].clear()
        else:
            self.__divs[root_u] |= self.__divs[root_v]
            self.__divs[root_v].clear()
            self.__divs[root_v] = self.__divs[root_u]

        if self.__sizes[root_v] >= target_size and div in self.__divs[root_v]:
            return {i for i in range(self.__len) if self.find(i) == root_v}


def get_divs(a, k):
    f = randint(1, 1 << 30)
    divs = set()
    for row in a:
        for ai in row:
            if k % ai == 0:
                divs.add(ai + f)
    return sorted([ai - f for ai in divs])


def subcomponent(component, h, w, a, div, target_size):
    y, x = next(divmod(i, w) for i in component if a[i // w][i % w] == div)
    stack = [(x, y)]
    res = [[0] * w for _ in range(h)]
    res[y][x] = div
    target_size -= 1
    while target_size > 0:
        x, y = stack.pop()
        for x2, y2 in [
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1),
        ]:
            i = y2 * w + x2
            if 0 <= x2 < w and 0 <= y2 < h and i in component and res[y2][x2] == 0:
                res[y2][x2] = div
                stack.append((x2, y2))
                target_size -= 1
                if target_size == 0:
                    break
    return res


def smart(h, w, k, a):
    if k > 10**15:
        return
    divs = get_divs(a, k)
    to_add = [[] for _ in range(len(divs))]
    for y in range(h):
        for x in range(w):
            ai = a[y][x]
            di = bisect_right(divs, ai)
            if di != 0:
                to_add[di - 1].append((x, y))
    uf = UnionFind(h * w, a, divs)
    for div, xy in reversed(list(zip(divs, to_add))):
        target_size = k // div
        if target_size == 1:
            res = [[0] * w for _ in range(h)]
            for y in range(h):
                for x in range(w):
                    if a[y][x] == div:
                        res[y][x] = div
                        return res
        for x, y in xy:
            i = y * w + x
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nx < w and 0 <= ny < h and a[ny][nx] >= div:
                    component = uf.union(i, ny * w + nx, target_size, div)
                    if component is not None:
                        return subcomponent(component, h, w, a, div, target_size)


def naive(h, w, k, a):
    divs = get_divs(a, k)
    for d in divs:
        target_size = k // d
        seen = [[False] * w for _ in range(h)]
        for y in range(h):
            for x in range(w):
                if seen[y][x] or a[y][x] != d:
                    continue
                seen[y][x] = True
                component = [(x, y)]
                stack = [(x, y)]
                while stack:
                    x2, y2 = stack.pop()
                    for x3, y3 in [
                        (x2 - 1, y2),
                        (x2 + 1, y2),
                        (x2, y2 - 1),
                        (x2, y2 + 1),
                    ]:
                        if (
                            0 <= x3 < w
                            and 0 <= y3 < h
                            and not seen[y3][x3]
                            and a[y3][x3] >= d
                        ):
                            seen[y3][x3] = True
                            component.append((x3, y3))
                            stack.append((x3, y3))
                if len(component) >= target_size:
                    res = [[0] * w for _ in range(h)]
                    for x, y in component[:target_size]:
                        res[y][x] = d
                    return res


def main():
    h, w, k = mir()
    a = [lmir() for _ in range(h)]
    res = smart(h, w, k, a)
    if res is None:
        print("NO")
    else:
        print("YES")
        for row in res:
            print(*row)


def test():
    seed(42)
    for _ in range(10000):
        print()
        h = randint(1, 10)
        w = randint(1, 10)
        mx = randint(1, 42)
        a = [choices(range(1, mx + 1), k=w) for _ in range(h)]
        k = randint(1, sum(map(sum, a)))

        rs = smart(h, w, k, a)
        rn = naive(h, w, k, a)
        if (rn is None) != (rs is None):
            print(h, w, k, a)
            if rn is None:
                print("smart solution:")
                print(*rs)
            else:
                print("naive solution:")
                print(*rn)
            return

        assert (rn is None) == (rs is None), (
            "naive has a solution" if rn else "smart has a solution"
        )
        if rs is None:
            continue
        if len(rs) != h or any(len(row) != w for row in rs) or sum(map(sum, rs)) != k:
            print(h, w, k, a, rs)
            print("INVALID")
            print(h, w, k, a)
            print(f"sum: {sum(map(sum,rs))}")
            print(*rs, sep="\n")
            return


if __name__ == "__main__":
    if sys.stdin.isatty():
        test()
    else:
        main()
