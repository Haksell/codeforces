# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, m = mir()
    left = 2 * n
    if m >= left:
        print("NO")
        return
    res = [[0] * m for _ in range(left)]
    for i in range(m):
        for c in range(n):
            res[(i + 2 * c) % left][i] = c + 1
            res[(i + 2 * c + 1) % left][i] = c + 1
    print("YES")
    for row in res:
        print(*row)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
