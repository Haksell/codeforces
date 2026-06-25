# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    print(1 + any(x + 1 == y for x, y in zip(a, a[1:])))
