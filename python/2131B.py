# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n = ir()
    a = [-1] * n
    for i in range(1, n, 2):
        a[i] = 3
    if n & 1 == 0:
        a[-1] = 2
    print(*a)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
