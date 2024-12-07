# ruff: noqa: E731, E741
def f(n):
    if n % 4 == 0:
        q = n >> 2
        return [q, q, q, q]
    elif n % 4 == 2:
        h = n >> 1
        return [h, h - 2, 1, 1]
    else:
        return [n - 4, 2, 1, 1]


for _ in range(int(input())):
    print(*f(int(input())))
