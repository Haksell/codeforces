for _ in range(int(input())):
    a, b, n = map(int, input().split())
    res = 0
    while a <= n and b <= n:
        if a < b:
            a += b
        else:
            b += a
        res += 1
    print(res)
