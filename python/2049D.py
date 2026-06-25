# ruff: noqa: E731, E741
from collections import deque
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

INF = 1 << 60


def solve():
    h, w, k = mir()
    dp = [INF] * w
    dp[0] = 0
    for _ in range(h):
        row = deque(mir())
        dps = []
        for move in range(w):
            new_cost = move * k
            new_dp = [-1] * w
            new_dp[0] = row[0] + dp[0] + new_cost
            for i in range(1, w):
                cost = row[i] + min(new_dp[i - 1], dp[i] + new_cost)
                new_dp[i] = cost
            dps.append(new_dp)
            row.append(row.popleft())
        dp = list(map(min, zip(*dps)))
    print(dp[-1])


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
