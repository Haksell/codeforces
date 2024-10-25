MOD = 1_000_000_007
n, k = map(int, input().split())
divisors = sorted({n // i for i in range(1, n + 1)})
div_idx = [len(divisors)] * (n + 1)
for i, d in enumerate(divisors):
    div_idx[d] = i

dp = [[int(i == 0)] * len(divisors) for i in range(k + 1)]
for kk in range(1, k + 1):
    for i, d in enumerate(divisors):
        dp[kk][i] = sum(dp[kk - 1][div_idx[d // i]] for i in range(1, d + 1)) % MOD
print(dp[-1][-1])
