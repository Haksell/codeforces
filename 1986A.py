# ruff: noqa: E731, E741
for _ in range(int(input())):
    x = list(map(int, input().split()))
    print(max(x) - min(x))
