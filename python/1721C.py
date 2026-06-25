# ruff: noqa: E731, E741
from bisect import bisect_right


def f(a, b, is_max):
    res = []
    for i, ai in reversed(list(enumerate(a))):
        j = bisect_right(b, ai - 0.5)
        res.append(b[-1 if is_max else j] - ai)
        if i == j:
            while len(b) > i:
                b.pop()
    return res[::-1]


for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(*f(a, b.copy(), False))
    print(*f(a, b, True))
