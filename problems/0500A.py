# ruff: noqa: E731, E741
n, t = map(int, input().split())
a = list(map(int, input().split()))

x = 0
while x < n - 1:
    x += a[x]
    if x == t - 1:
        print("YES")
        exit()
print("NO")
