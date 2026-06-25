# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    print(sum(a[(n + 1) >> 1 :]) - sum(a[: n >> 1]))
