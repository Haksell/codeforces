# ruff: noqa: E731, E741
from itertools import groupby
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def score(group):
    res = cur = 0
    for n in group:
        cur = max(cur + n, 0)
        res = max(res, cur)
    return res or max(group)


def main():
    for _ in rir():
        n = ir()
        a = lmir()
        groups = [
            [a[i] for i in v]
            for _, v in groupby(range(n), key=lambda i: (i ^ a[i]) & 1)
        ]
        print(max(map(score, groups)))


if __name__ == "__main__":
    main()
