# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    print(m + (sum(a) - m) / (n - 1))
