# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b, k = map(int, input().split())
    print((k + 1) // 2 * a - k // 2 * b)
