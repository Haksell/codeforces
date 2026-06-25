# ruff: noqa: E731, E741
for _ in range(int(input())):
    x, n = map(int, input().split())
    change = [0, -n, 1, n + 1][n & 3]
    print(x - change if x & 1 else x + change)
