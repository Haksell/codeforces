# ruff: noqa: E731, E741
from itertools import count
from random import randint
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    _, m = mir()
    f = randint(1, 1 << 30)
    s = {x + f for x in mir()}
    res = []
    for i in count(1):
        if i > m:
            break
        if i + f not in s:
            m -= i
            res.append(i)
    print(len(res))
    print(*res)


if __name__ == "__main__":
    main()
