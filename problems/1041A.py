# ruff: noqa: E731, E741
n = int(input())
a = list(map(int, input().split()))
print(max(a) - min(a) - n + 1)
