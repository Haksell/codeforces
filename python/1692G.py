# ruff: noqa: E731, E741
from itertools import accumulate
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, k = mir()
    a = lmir()
    b = [x < y * 2 for x, y in zip(a, a[1:])]
    acc = list(accumulate(b, initial=0))
    print(sum(acc[i + k] - acc[i] == k for i in range(n - k)))


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
