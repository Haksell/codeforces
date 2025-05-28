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
    s = input()
    o = s.count("1")
    print(o * (n - 2) + n)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
