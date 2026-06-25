# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def f(inside, outside):
    s = sum(inside)
    for i, o in zip(sorted(inside, reverse=True), sorted(outside)):
        if o > i:
            break
        s -= i - o
    return s


def solve():
    _, l, r = mir()
    a = lmir()
    left = a[: l - 1]
    middle = a[l - 1 : r]
    right = a[r:]
    print(min(f(middle, left), f(middle, right)))


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
"5 6 2     1 7 8 9     4 5 6 2 3"
"          l     r              "
"4"
"2"
