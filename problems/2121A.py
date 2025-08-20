# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, s = mir()
    xs = lmir()
    mini = min(xs)
    maxi = max(xs)
    if s <= mini:
        print(maxi - s)
    elif s >= maxi:
        print(s - mini)
    else:
        print(maxi - mini + min(maxi - s, s - mini))


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
