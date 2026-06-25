# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def sum_range(a, b):
    return (a + b) * (b - a + 1) >> 1


def main():
    for _ in rir():
        n, k = mir()
        print("YES" if sum_range(n - k + 1, n) & 1 == 0 else "NO")


if __name__ == "__main__":
    main()
