# ruff: noqa: E731, E741
from collections import Counter
from random import randint
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    _, k = mir()
    a = lmir()
    f = randint(1 << 29, 1 << 30)
    v = sorted(Counter(ai + f for ai in a).values(), reverse=True)
    while v and k >= v[-1]:
        k -= v.pop()
    print(max(1, len(v)))


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
