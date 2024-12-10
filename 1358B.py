# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    a = sorted(map(int, input().split()))
    print(max((i for i, n in enumerate(a, 1) if n <= i), default=0) + 1)
