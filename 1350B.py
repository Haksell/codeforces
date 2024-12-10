# ruff: noqa: E731, E741
import sys


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    s = list(map(int, sys.stdin.readline().split()))
    dp = [1] * n
    for i in range(n >> 1, -1, -1):
        for j in range(2 * i + 1, n, i + 1):
            if s[j] > s[i]:
                dp[i] = max(dp[i], 1 + dp[j])
    print(max(dp))
