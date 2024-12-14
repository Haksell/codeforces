# ruff: noqa: E731, E741
k = int(input())
a = sorted(list(map(int, input().split())))
res = 0
while a and k > 0:
    res += 1
    k -= a.pop()
print(-1 if k > 0 else res)
