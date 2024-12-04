from collections import Counter
import sys
read = sys.stdin.readline
write = lambda x, end="\n": sys.stdout.write(x + end)

for _ in range(int(input())):
    n = int(input())
    m = n // 3
    l = list(map(int, input().split()))
    x = [x % 3 for x in l]
    c = Counter(x)
    d = [c[i] for i in range(3)]
    res = 1 << 28
    for j in range(3):
        c = d.copy()
        # print(c)
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
        # print(c)
        else:
            res = min(res, z)
        # print()
    print(res)
    # print()