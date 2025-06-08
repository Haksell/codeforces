# ruff: noqa: E731, E741
from itertools import accumulate
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n, k, q = mir()
    e = [0] * (200_002)
    for _ in range(n):
        l, r = mir()
        e[l] += 1
        e[r + 1] -= 1
    counts = list(accumulate(e))
    good = [c >= k for c in counts]
    acc = list(accumulate(good))
    for _ in range(q):
        a, b = mir()
        print(acc[b] - acc[a - 1])


if __name__ == "__main__":
    main()
