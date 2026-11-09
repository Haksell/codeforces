from itertools import accumulate

for _ in range(int(input())):
    n, k = map(int, input().split())
    asum = accumulate(map(int, input().split()))
    bmax = accumulate(map(int, input().split()), max)
    print(max(ai + bi * (k - i - 1) for i, ai, bi in zip(range(k), asum, bmax)))
