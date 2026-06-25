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
    a = [int(input().split(" ", 2)[0]) for _ in range(n - 1)] + lmir()
    is_present = [False] * (2 * n)
    for ai in a:
        is_present[ai - 1] = True
    absent = 1 + next(i for i, p in enumerate(is_present) if not p)
    print(absent, *a)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
