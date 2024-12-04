from itertools import count


def f(n, m):
    for i in count(1):
        if n == 0:
            return i - 1
        if i % m != 0:
            n -= 1


a, b = map(int, input().split())
print(f(a, b))
