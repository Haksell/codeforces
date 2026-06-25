# ruff: noqa: E731, E741
from itertools import chain
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = ir()
    a = list(range(1, n + 1))
    c = lmir()
    res = []
    for car in reversed(c):
        i = a.index(car)
        for j in chain(reversed(range(i)), range(n - 1)):
            a[j], a[j + 1] = a[j + 1], a[j]
            res.append((a[j], a[j + 1]))
        n -= 1
    print(len(res))
    for x, y in res:
        print(x, y)


if __name__ == "__main__":
    main()
