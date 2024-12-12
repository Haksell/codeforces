# ruff: noqa: E731, E741
n = int(input())
if n > 0:
    print(n)
else:
    a = -n
    x = a // 10
    y = a // 100 * 10 + a % 10
    print(-min(x, y))
