# ruff: noqa: E731, E741
from statistics import median_high
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n = ir()
        a = lmir()
        print(-1 if n <= 2 else max(0, median_high(a) * 2 * n + 1 - sum(a)))


if __name__ == "__main__":
    main()
