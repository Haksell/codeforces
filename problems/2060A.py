# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    a1, a2, a4, a5 = mir()
    r = 0
    for a3 in range(-200, 200):
        f = (a1 + a2 == a3) + (a2 + a3 == a4) + (a3 + a4 == a5)
        r = max(r, f)
    print(r)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
