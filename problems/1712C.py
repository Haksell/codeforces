# ruff: noqa: E731, E741
from collections import Counter
from itertools import groupby
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        read()
        a = lmir()
        g = [k for k, _ in groupby(a)]
        cnt = Counter(g)
        k = 0
        m = g[-1]
        for x in reversed(g):
            if cnt[x] >= 2 or x > m:
                break
            m = x
            k += 1
        print(len(set(g)) - k)


if __name__ == "__main__":
    main()
