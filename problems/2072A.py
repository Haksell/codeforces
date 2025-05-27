# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def int_ceil(x, y):
    return (x + y - 1) // y


def solve():
    n, k, p = mir()
    k = abs(k)
    print(-1 if k > n * p else int_ceil(k, p))


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
