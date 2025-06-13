# ruff: noqa: E731, E741
from math import lcm
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(k):
    l = lcm(*k)
    res = [l // ki for ki in k]
    return res if sum(res) < l else None


def main():
    for _ in rir():
        read()
        k = lmir()
        res = solve(k)
        if res is None:
            print(-1)
        else:
            print(*res)


if __name__ == "__main__":
    main()
