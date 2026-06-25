# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    print(max(x * y for x, y in zip(a, a[1:])))
