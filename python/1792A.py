# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    print(n - h.count(1) // 2)
