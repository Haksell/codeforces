from collections import Counter
from math import nan

n = int(input())
counter = sorted(Counter(list(map(int, input().split()))).items())
dp = [0] * (len(counter) + 1)
last_val = nan
for i, (val, count) in enumerate(counter, 1):
    if i == 1:
        dp[i] = val * count
    else:
        take_current = val * count + dp[i - 2 if last_val + 1 == val else i - 1]
        dp[i] = max(dp[i - 1], take_current)
    last_val = val
print(dp[-1])
