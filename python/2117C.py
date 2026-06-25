# ruff: noqa: E731, E741
from random import randint
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    read()
    a = lmir()
    f = randint(1, 1 << 30)
    a = [ai + f for ai in a]
    cur = set()
    required = set()
    remaining = set()
    res = 0
    for ai in a:
        remaining.discard(ai)
        cur.add(ai)
        if not remaining:
            res += 1
            required |= cur
            remaining = required.copy()
            cur.clear()
    print(res)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
