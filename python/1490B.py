from collections import Counter

for _ in range(int(input())):
    n = int(input())
    m = n // 3
    a = list(map(int, input().split()))
    x = [x % 3 for x in a]
    c = Counter(x)
    d = [c[i] for i in range(3)]
    res = 1 << 28
    for j in range(3):
        c = d.copy()
        z = 0
        for i in range(3):
            i = (i + j) % 3
            if c[i] > m:
                x = c[i] - m
                z += x
                c[(i + 1) % 3] += x
                c[i] -= x
            elif c[i] < m:
                break
        else:
            res = min(res, z)
    print(res)
