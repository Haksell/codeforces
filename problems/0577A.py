# ruff: noqa: E731, E741
n, x = map(int, input().split())
res = 0
for i in range(1, n + 1):
    if x % i == 0:
        j = x // i
        if i == j:
            res += 1
        elif i < j <= n:
            res += 2
print(res)
