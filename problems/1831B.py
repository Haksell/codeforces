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


def longest():
    cnt = Counter()
    for k, v in groupby(mir()):
        cnt[k] = max(cnt[k], sum(1 for _ in v))
    return cnt


def main():
    for _ in rir():
        read()
        print(max((longest() + longest()).values()))


if __name__ == "__main__":
    main()
