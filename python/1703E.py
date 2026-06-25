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
    a = [list(map(int, input())) for _ in range(n)]
    res = 0
    for y in range((n + 1) // 2):
        for x in range(n // 2):
            c1 = a[y][x]
            c2 = a[x][n - y - 1]
            c3 = a[n - y - 1][n - x - 1]
            c4 = a[n - x - 1][y]
            cnt = c1 + c2 + c3 + c4
            res += min(cnt, 4 - cnt)
    print(res)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()

"""
aaabb
aaabb
dd bb
ddccc
ddccc
"""
