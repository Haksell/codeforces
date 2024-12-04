n, m = map(int, input().split())
res = 0
while n != m:
    if m & 1 or m < n:
        m += 1
    else:
        m >>= 1
    res += 1
print(res)