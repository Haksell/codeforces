lim = 10**6 + 1
dp = [False] * lim
dp[0] = True
for i in range(2020, lim):
    dp[i] = dp[i - 2020] or dp[i - 2021]

for _ in range(int(input())):
    print("YES" if dp[int(input())] else "NO")
