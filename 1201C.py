import sys

n, k = map(int, input().split())
half = sorted(map(int, input().split()))[n >> 1 : n]
for i, (a, b) in enumerate(zip(half, half[1:]), 1):
    d = b - a
    if i * d > k:
        print(a + k // i)
        sys.exit()
    k -= i * d
print(half[-1] + k // len(half))
