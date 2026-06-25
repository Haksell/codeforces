# ruff: noqa: E731, E741
n = int(input())
a = sorted(set(map(int, input().split())))
print("NO" if len(a) < 2 else a[1])
