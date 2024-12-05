# ruff: noqa: E731, E741
n, m = map(int, input().split())
a = [int(x) - 1 for x in input().split()]
a.insert(0, 0)
print(sum((y - x) % n for x, y in zip(a, a[1:])))
