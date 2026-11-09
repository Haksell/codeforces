for _ in range(int(input())):
    n, m, k, H = map(int, input().split())
    maxi = (m - 1) * k
    res = 0
    for hi in map(int, input().split()):
        diff = abs(H - hi)
        res += diff % k == 0 and diff > 0 and diff <= maxi
    print(res)
