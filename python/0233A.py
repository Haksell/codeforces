# ruff: noqa: E731, E741
n = int(input())
if n & 1:
    print(-1)
else:
    print(*[n - i for i in range(n)])
