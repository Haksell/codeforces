for _ in range(int(input())):
    w, h, n = map(int, input().split())
    res = 1
    while w & 1 == 0:
        res <<= 1
        w >>= 1
    while h & 1 == 0:
        res <<= 1
        h >>= 1
    print("YES" if res >= n else "NO")
