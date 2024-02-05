from math import isqrt


for _ in range(int(input())):
    input()
    z = sum(map(int, input().split()))
    i = isqrt(z)
    print("YES" if i * i == z else "NO")
