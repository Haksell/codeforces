# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = [tuple(map(int, input().split())) for _ in range(n)]
    print(max(range(n), key=lambda i: (a[i][0] <= 10) * a[i][1]) + 1)
