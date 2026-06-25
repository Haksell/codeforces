# ruff: noqa: E731, E741
from collections import Counter


def f(a, k):
    counter = Counter(a)
    if len(counter) > k:
        return None
    pattern = list(counter.keys())
    duplicates = [n for n, count in counter.items() for _ in range(count - 1)]
    pattern.extend(duplicates[: k - len(counter)])
    return pattern * (10000 // k)


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = f(a, k)
    if b is None:
        print(-1)
    else:
        print(len(b))
        print(*b)
