# ruff: noqa: E731, E741
from collections import Counter
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        nb, ng, k = mir()
        b = lmir()
        g = lmir()
        cb = Counter(b)
        cg = Counter(g)
        print(sum(k - cb[b[i]] - cg[g[i]] + 1 for i in range(k)) >> 1)


if __name__ == "__main__":
    main()
