# ruff: noqa: E731, E741
x, y = map(int, input().split())
n = (int(input()) - 2) % 6
for _ in range(n):
    x, y = y, y - x
print(y % 1_000_000_007)
