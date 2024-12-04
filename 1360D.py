from math import ceil

for _ in range(int(input())):
    n, p = map(int, input().split())
    if p >= n:
        print(1)
    else:
        z = n
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                if i <= p:
                    z = min(z, n // i)
                if n // i <= p:
                    z = min(z, i)
        print(z)
