# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, _ = map(int, input().split())
    if n & 3 == 0:
        print(n >> 2, n >> 2, n >> 1)
    else:
        mul = 1
        if n & 1 == 0:
            n >>= 1
            mul = 2
        big = (n >> 1) * mul
        print(mul, big, big)
