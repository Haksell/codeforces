def naive(n, k):
    a = n - 1
    b = 0
    for _ in range(k - 1):
        a = (a - 1) % n
        b = (b + 1) % n
        if a == b:
            b = (b + 1) % n
    return b + 1


def f(n, k):
    res = (k - 1) % n + 1
    if n & 1 == 0:
        return res
    else:
        diff = (k - 1) // (n // 2)
        return (res - 1 + diff) % n + 1


for _ in range(int(input())):
    n, k = map(int, input().split())
    print(f(n, k))
