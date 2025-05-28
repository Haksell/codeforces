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
    eyes = input().count("-")
    mouths = n - eyes
    e1 = eyes >> 1
    e2 = eyes - e1
    print(e1 * mouths * e2)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
