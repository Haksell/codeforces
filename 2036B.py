# ruff: noqa: E731
from collections import defaultdict
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
        d = defaultdict(int)
        for _ in range(k):
            b, c = mir()
            d[b] += c
        print(sum(sorted(d.values(), reverse=True)[:n]))


if __name__ == "__main__":
    main()
