# TODO: actually

MOD = 1_000_000_007

n, k = map(int, input().split())

dp = [[0] * (n + 1) for _ in range(k + 1)]
dp[0] = [1] * (n + 1)
for i in range(1, k + 1):
    for j in range(n + 1):
        dp[i][j] = sum(dp[i - 1][j // x] for x in range(1, j + 1)) % MOD
print(dp[-1][-1])
