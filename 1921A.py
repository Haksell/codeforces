# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print((a - c if a != c else b - d) ** 2)
    input()
    input()
