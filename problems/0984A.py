# ruff: noqa: E731, E741
from statistics import median_low
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    read()
    a = lmir()
    print(median_low(a))


if __name__ == "__main__":
    main()
