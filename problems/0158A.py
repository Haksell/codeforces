# ruff: noqa: E731, E741
n, k = map(int, input().split())
a = list(map(int, input().split()))
print(sum(x > 0 and x >= a[k - 1] for x in a))
