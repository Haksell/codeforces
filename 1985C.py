for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = m = res = 0
    for ai in a:
        s += ai
        m = max(m, ai)
        res += m << 1 == s
    print(res)
