# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    read()
    a = set(mir())
    print("NO" if 1 in a and (0 in a or any(x + 1 in a for x in a)) else "YES")


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
