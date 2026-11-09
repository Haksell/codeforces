from itertools import groupby


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = sum(k and any(v) for k, v in groupby(a, key=lambda x: x <= 0))
    print(sum(map(abs, a)), res)
