# ruff: noqa: E731, E741
from math import gcd
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = ir()
    print(sum(gcd(i, n) == 1 for i in range(1, n + 1)))


if __name__ == "__main__":
    main()
