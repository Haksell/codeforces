# ruff: noqa: E731, E741
from itertools import combinations
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n, l, r, x = mir()
    c = sorted(mir())
    res = 0
    for i in range(2, n + 1):
        for comb in combinations(c, r=i):
            res += comb[-1] - comb[0] >= x and l <= sum(comb) <= r
    print(res)


if __name__ == "__main__":
    main()
