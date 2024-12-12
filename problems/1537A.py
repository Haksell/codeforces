# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    s = sum(map(int, input().split()))
    print(1 if s < n else s - n)
