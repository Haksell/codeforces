# ruff: noqa: E731, E741
from itertools import count
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    read()
    s = set(mir())
    print(next(i for i in count(1) if i not in s))


if __name__ == "__main__":
    main()
