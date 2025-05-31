# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    s = input()
    t = s.rstrip("0")
    x = t.count("0") + 1
    print(len(s) - x)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
