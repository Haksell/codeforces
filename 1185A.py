# ruff: noqa: E731, E741
*r, d = map(int, input().split())
a, b, c = sorted(r)
print(max(0, d - (b - a)) + max(0, d - (c - b)))
