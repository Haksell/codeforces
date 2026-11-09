from itertools import islice


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = min(y - x for x, y in zip(a, islice(a, 1, None)))
    print(max(0, (m >> 1) + 1))
