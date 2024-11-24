# ruff: noqa: E731
from heapq import nlargest
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n, k = mir()
        d = [0] * k
        for _ in range(k):
            b, c = mir()
            d[b - 1] += c
        print(sum(nlargest(n, d)))


if __name__ == "__main__":
    main()
