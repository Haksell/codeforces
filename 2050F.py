# ruff: noqa: E731, E741
from math import gcd
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


class SegmentTree:
    def __init__(self, data, *, func=int.__add__, default=0):
        self.__func = func
        self.__default = default
        self.__n = len(data)
        self.__tree = [self.__default] * (2 * self.__n)
        for i in range(self.__n):
            self.__tree[self.__n + i] = data[i]
        for i in range(self.__n - 1, 0, -1):
            self.__tree[i] = func(self.__tree[i << 1], self.__tree[i << 1 | 1])

    def __len__(self):
        return self.__n

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__tree[self.__n:]})"

    def __getitem__(self, i):
        return self.__tree[i + self.__n]

    def __setitem__(self, i, value):
        i += self.__n
        self.__tree[i] = value
        while i > 1:
            i >>= 1
            self.__tree[i] = self.__func(self.__tree[i << 1], self.__tree[i << 1 | 1])

    def range_query(self, left, right):
        left += self.__n
        right += self.__n
        res = self.__default
        while left < right:
            if left & 1:
                res = self.__func(self.__tree[left], res)
                left += 1
            if right & 1:
                right -= 1
                res = self.__func(self.__tree[right], res)
            left >>= 1
            right >>= 1
        return res

    def full_query(self):
        return self.__default if self.__n == 0 else self.__tree[1]


def main():
    for _ in rir():
        n, q = mir()
        a = lmir()
        d = [abs(a[i] - a[i - 1]) for i in range(1, n)]
        st = SegmentTree(d, func=gcd, default=0)
        res = []
        for _ in range(q):
            l, r = mir()
            res.append(st.range_query(l - 1, r - 1))
        print(*res)


if __name__ == "__main__":
    main()
