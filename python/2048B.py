# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, k = mir()
    r = [-1] * n
    x = 1
    for i in range(k - 1, n, k):
        r[i] = x
        x += 1
    for i in range(n):
        if r[i] == -1:
            r[i] = x
            x += 1
    print(*r)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
