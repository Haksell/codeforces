# ruff: noqa: E731, E741
from itertools import count, product
from string import ascii_lowercase
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(n, s):
    for size in count(1):
        seen = {s[i : i + size] for i in range(n - size + 1)}
        for tup in product(ascii_lowercase, repeat=size):
            tup = "".join(tup)
            if tup not in seen:
                return tup


def main():
    for _ in rir():
        print(solve(ir(), input()))


if __name__ == "__main__":
    main()
