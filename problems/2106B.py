# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, x = mir()
    res = list(range(x)) + list(range(n - 1, x - 1, -1))
    print(*res)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
