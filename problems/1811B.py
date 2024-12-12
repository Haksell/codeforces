# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def f(n, x, y):
    return min(x, y, n + 1 - x, n + 1 - y)


def main():
    for _ in rir():
        n, x1, y1, x2, y2 = mir()
        print(abs(f(n, x1, y1) - f(n, x2, y2)))


if __name__ == "__main__":
    main()
