# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(n):
    return list(range(1, n + 1, 2)) + list(range(n & ~1, 1, -2))


def main():
    for _ in rir():
        print(*solve(ir()))


if __name__ == "__main__":
    main()
