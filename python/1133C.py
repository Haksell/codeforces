n = int(input())
a = sorted(map(int, input().split()))
lo = 0
res = 1
for hi in range(n):
    while a[hi] - a[lo] > 5:
        lo += 1
    res = max(res, hi - lo + 1)
print(res)
