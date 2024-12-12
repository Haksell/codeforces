# ruff: noqa: E731, E741
n = int(input())
a = sorted(map(int, input().split()))
print(sum(y - x for x, y in zip(a[::2], a[1::2])))
