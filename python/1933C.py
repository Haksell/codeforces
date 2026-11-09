def f(n, d):
    res = {n}
    while n % d == 0:
        n //= d
        res.add(n)
    return res


def g(n, a, b):
    res = f(n, b)
    while n % a == 0:
        n //= a
        res |= f(n, b)
    return res


for _ in range(int(input())):
    a, b, n = map(int, input().split())
    res = g(n, a, b) | g(n, b, a)
    print(len(res))
