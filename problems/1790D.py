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


def main():
    for _ in rir():
        read()
        a = lmir()
        x = randint(1, 1 << 30)
        c = Counter(ai + x for ai in a)
        pk = pv = 0
        res = 0
        for k, v in sorted(c.items()):
            if k != pk + 1:
                res += pv
            else:
                res += max(0, pv - v)
            pk = k
            pv = v
        res += pv
        print(res)


if __name__ == "__main__":
    main()
