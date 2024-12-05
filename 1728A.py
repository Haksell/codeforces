# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    cnt = list(map(int, input().split()))
    print(max(range(n), key=cnt.__getitem__) + 1)
