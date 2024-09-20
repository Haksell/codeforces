from itertools import count


def ceil_div(numer, denom):
    return (numer + denom - 1) // denom


for _ in range(int(input())):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    start = 0
    for i in count(1):
        try:
            start = p.index(i, start)
        except ValueError:
            print(ceil_div(n - (i - 1), k))
            break
