# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    a, b, *_, c, d = sorted(map(int, input().split()))
    print(d + c - b - a << 1)
