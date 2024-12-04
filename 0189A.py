# from functools import lru_cache
from math import inf

n, a, b, c = map(int, input().split())


dp = [0]
for i in range(1, n + 1):
    dp.append(
        max(
            -inf if a > i else dp[i - a],
            -inf if b > i else dp[i - b],
            -inf if c > i else dp[i - c],
        )
        + 1
    )
print(dp[-1])
