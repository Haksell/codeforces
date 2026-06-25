# ruff: noqa: E731, E741
def int_ceil(n, k):
    return (n + k - 1) // k


for _ in range(int(input())):
    x, y, k = map(int, input().split())
    print(max(2 * int_ceil(x, k) - 1, 2 * int_ceil(y, k)))
