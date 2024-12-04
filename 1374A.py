for _ in range(int(input())):
    x, y, n = map(int, input().split())
    res = n // x * x + y
    if res > n:
        res -= x
    print(res)
