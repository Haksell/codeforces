# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


class FenwickTree:
    def __init__(self, size):
        self.__len = size
        self.__tree = [0] * (size + 1)

    def __len__(self):
        return self.__len

    def update(self, i, delta):
        i += 1
        while i <= self.__len:
            self.__tree[i] += delta
            i += i & -i

    def prefix_sum(self, i):
        res = 0
        while i > 0:
            res += self.__tree[i]
            i -= i & -i
        return res


def main():
    read()
    a = lmir()
    indices = sorted(range(len(a)), key=a.__getitem__)
    for compressed, i in enumerate(indices):
        a[i] = compressed
    fenwick_tree = FenwickTree(len(a))
    inv = 0
    for i, ai in enumerate(a):
        inv += i - fenwick_tree.prefix_sum(ai + 1)
        fenwick_tree.update(ai, 1)
    print(inv)


if __name__ == "__main__":
    main()
