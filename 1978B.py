# ruff: noqa: E731, E741
def sum_range(a, b):
    return (a + b) * (b - a + 1) >> 1


for _ in range(int(input())):
    n, a, b = map(int, input().split())
    k = min(max(0, b - a), n)
    print((n - k) * a + sum_range(b - k + 1, b))
