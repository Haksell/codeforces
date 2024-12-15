# ruff: noqa: E731, E741
from math import inf
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def extract_divisor(numer, denom):
    if numer == 0:
        return inf
    ans = 0
    while numer % denom == 0:
        numer //= denom
        ans += 1
    return ans


def get_dp(n, m, d):
    dp = [[extract_divisor(x, d) for x in r] for r in m]
    for i in range(1, n):
        dp[0][i] += dp[0][i - 1]
        dp[i][0] += dp[i - 1][0]
    for y in range(1, n):
        for x in range(1, n):
            dp[y][x] += min(dp[y - 1][x], dp[y][x - 1])
    return dp


def get_min_path(dp):
    y = x = len(dp) - 1
    path = []
    while y > 0 and x > 0:
        if dp[y - 1][x] < dp[y][x - 1]:
            y -= 1
            path.append("D")
        else:
            x -= 1
            path.append("R")
    path.extend(["R"] * x)
    path.extend(["D"] * y)
    return "".join(reversed(path))


def get_zero_path(m):
    y = next(y for y, r in enumerate(m) if 0 in r)
    moves = len(m) - 1
    return "D" * y + "R" * moves + "D" * (moves - y)


def main():
    n = ir()
    m = [lmir() for _ in range(n)]
    dp2 = get_dp(n, m, 2)
    dp5 = get_dp(n, m, 5)
    dp = dp2 if dp2[-1][-1] < dp5[-1][-1] else dp5
    if dp[-1][-1] > 0 and any(0 in row for row in m):
        print(1)
        print(get_zero_path(m))
    else:
        print(dp[-1][-1])
        print(get_min_path(dp))


if __name__ == "__main__":
    main()
