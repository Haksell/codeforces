# ruff: noqa: E731, E741
def triangle(n):
    return n * (n + 1) >> 1


for _ in range(int(input())):
    n, r = map(int, input().split())
    print(triangle(min(r, n - 1)) + (n <= r))
