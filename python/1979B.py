# ruff: noqa: E731, E741
for _ in range(int(input())):
    x, y = map(int, input().split())
    d = abs(x - y)
    print(d ^ (d & (d - 1)))
