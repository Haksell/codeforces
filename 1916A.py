import math

for _ in range(int(input())):
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    p = math.prod(b)
    q, r = divmod(2023, p)
    if r == 0:
        print("YES")
        print(q, *([1] * (k - 1)))
    else:
        print("NO")
