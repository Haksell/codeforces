from itertools import accumulate


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    acc = list(accumulate(a, initial=0))
    s = input()
    res = 0
    lo = 0
    hi = n - 1
    while lo < hi:
        while lo < hi and s[lo] == "R":
            lo += 1
        while lo < hi and s[hi] == "L":
            hi -= 1
        if lo >= hi:
            break
        res += acc[hi + 1] - acc[lo]
        lo += 1
        hi -= 1
    print(res)
