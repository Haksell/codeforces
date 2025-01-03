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
    r = 1
    while n >= 4:
        n >>= 2
        r <<= 1
    print(r)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
