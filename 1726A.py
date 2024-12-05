# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(0)
        continue
    x1 = max(a[1:]) - a[0]
    x2 = a[-1] - min(a[:-1])
    x3 = max(a1 - a2 for a1, a2 in zip(a, a[1:] + [a[0]]))
    print(max(x1, x2, x3))
