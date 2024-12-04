from itertools import chain


def f(a, b, c, d):
    return a < b < d and a < c < d


for _ in range(int(input())):
    a, b, c, d = map(int, chain(input().split(), input().split()))
    print(
        "YES"
        if f(a, b, c, d) or f(b, d, a, c) or f(d, c, b, a) or f(c, a, d, b)
        else "NO"
    )
