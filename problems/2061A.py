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
    a = lmir()
    o = sum(ai & 1 for ai in a)
    e = n - o
    if e == 0:
        print(n - 1)
    else:
        print(1 + o)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
