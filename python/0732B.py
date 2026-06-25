# ruff: noqa: E731, E741
n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i, x in enumerate(a[1:], 1):
    d = k - (x + a[i - 1])
    if d > 0:
        ans += d
        a[i] += d
print(ans)
print(*a)
