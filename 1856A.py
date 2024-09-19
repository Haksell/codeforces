for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = a[0]
    res = 0
    for ai in a[1:]:
        if ai >= m:
            m = ai
        else:
            res = m
    print(res)
