from collections import Counter


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = Counter(Counter(a).values())
    res = n
    last = 1 << 28
    count = 0
    tot = 0
    x = 0
    for k, v in sorted(s.items(), reverse=True):
        tot += (last - k) * count
        cand = tot + (n - x - k * v)
        res = min(res, cand)
        last = k
        count += v
        x += k * v
    print(res)
