# ruff: noqa: E731, E741
n, k = map(int, input().split())
a = sorted(map(int, input().split()))
if k == 0:
    print(-1 if a[0] == 1 else 1)
elif k < n and a[k - 1] == a[k]:
    print(-1)
else:
    print(a[k - 1])
