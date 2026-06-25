# ruff: noqa: E731, E741
def f(n, x, y):
    return max(0, max(x, y) + 1 - n)


for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(f(a, b, c), f(b, c, a), f(c, a, b))
