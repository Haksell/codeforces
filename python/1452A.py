# ruff: noqa: E731, E741
for _ in range(int(input())):
    x, y = map(int, input().split())
    print(x + y if x == y else 2 * max(x, y) - 1)
