# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(n, a, b):
    x = a[::2].count("0") + b[1::2].count("0")
    y = a[1::2].count("0") + b[::2].count("0")
    return x >= (n + 1) // 2 and y >= n // 2


def main():
    for _ in rir():
        n = ir()
        a = input()
        b = input()
        print("YES" if solve(n, a, b) else "NO")


if __name__ == "__main__":
    main()
