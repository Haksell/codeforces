# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k == 1:
        print(n - 1 >> 1)
    else:
        print(sum(y > x + z for x, y, z in zip(a, a[1:], a[2:])))
