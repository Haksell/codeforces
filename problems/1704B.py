# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, x = mir()
    a = lmir()
    res = 0
    mini = maxi = a[0]
    for ai in a[1:]:
        mini = min(mini, ai)
        maxi = max(maxi, ai)
        if maxi - mini > 2 * x:
            res += 1
            mini = maxi = ai
    print(res)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
