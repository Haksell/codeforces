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
    y, w = mir()
    n = 7 - max(y, w)
    g = gcd(n, 6)
    print(f"{n//g}/{6//g}")


if __name__ == "__main__":
    main()
