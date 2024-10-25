MOD = 1_000_000_007

n, k = map(int, input().split())
divisors = sorted({n // i for i in range(1, n + 1)})
div_idx = [len(divisors)] * (n + 1)
for i, d in enumerate(divisors):
    div_idx[d] = i

dp = [1] * len(divisors)
for _ in range(k):
    dp = [sum(dp[div_idx[d // i]] for i in range(1, d + 1)) % MOD for d in divisors]
print(dp[-1])
