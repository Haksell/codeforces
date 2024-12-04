from random import randint
import sys
read = sys.stdin.readline
write = lambda x, end="\n": sys.stdout.write(x + end)


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


# for n in range(3, 11, 2):
#     for k in range(1, 11):
#         print(n, k, naive(n, k), f(n, k), (f(n, k) - naive(n, k)) % n)
#     print()

input()
for line in sys.stdin:
    n, k = map(int, line.split())
    print(f(n, k))