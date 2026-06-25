# ruff: noqa: E731, E741
n = int(input())
if n <= 3:
    print(0, 0, n)
else:
    a, b, c = 2, 3, 5
    while c != n:
        a, b, c = b, c, b + c
    print(0, a, b)
