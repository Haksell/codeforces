# ruff: noqa: E731, E741
n = int(input())
a = list(map(int, input().split()))
print(["chest", "biceps", "back"][max(range(3), key=lambda i: sum(a[i::3]))])
