# ruff: noqa: E731, E741
for _ in range(int(input())):
    c, m, x = map(int, input().split())
    print(min(c, m, (c + m + x) // 3))