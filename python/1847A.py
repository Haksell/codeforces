# ruff: noqa: E731, E741
from heapq import nsmallest
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n, k = mir()
        a = lmir()
        d = [abs(x - y) for x, y in zip(a, a[1:])]
        print(sum(nsmallest(n - k, d)))


if __name__ == "__main__":
    main()
