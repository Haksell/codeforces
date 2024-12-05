# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def iterative(a, b, c):
    na = len(a) + 1
    nb = len(b) + 1
    dp = [[-1] * nb for _ in range(na)]
    for ia in range(na):
        dp[ia][-1] = sum(a[i] != c[i + len(b)] for i in range(ia, len(a)))
    for ib in range(nb):
        dp[-1][ib] = sum(b[i] != c[i + len(a)] for i in range(ib, len(b)))
    for ia in range(na - 2, -1, -1):
        for ib in range(nb - 2, -1, -1):
            ra = dp[ia + 1][ib] + (a[ia] != c[ia + ib])
            rb = dp[ia][ib + 1] + (b[ib] != c[ia + ib])
            dp[ia][ib] = min(ra, rb)
    return dp[0][0]


def main():
    for _ in rir():
        a = input()
        b = input()
        c = input()
        print(iterative(a, b, c))


if __name__ == "__main__":
    main()
