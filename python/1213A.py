# ruff: noqa: E731, E741
n = int(input())
xs = list(map(int, input().split()))
s = sum(x & 1 for x in xs)
print(min(s, n - s))
