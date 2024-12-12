# ruff: noqa: E731, E741
from collections import Counter
from random import randint
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        x = randint(1, 1 << 30)
        n = ir()
        m = max(Counter(y ^ x for y in mir()).values())
        if m == n:
            print(0)
            continue
        r = n - m
        while m < n:
            r += 1
            m <<= 1
        print(r)


if __name__ == "__main__":
    main()
