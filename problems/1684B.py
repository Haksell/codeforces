# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(a + b + c, b + c, c)
