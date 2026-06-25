# ruff: noqa: E731, E741
input()
print(*[~-int(n) | 1 for n in input().split()])
