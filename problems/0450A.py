# ruff: noqa: E731, E741
def ceil_div(a, b):
    return -(-a // b)


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = [ceil_div(ai, m) for ai in a]
print(max(range(n), key=lambda i: (b[i], i)) + 1)
