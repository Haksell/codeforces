# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mini = min(range(n), key=a.__getitem__)
    maxi = max(range(n), key=a.__getitem__)
    x, y = sorted([mini, maxi])
    left = y + 1
    right = n - x
    both = (x + 1) + (n - y)
    print(min(left, right, both))
