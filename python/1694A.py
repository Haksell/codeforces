# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b = map(int, input().split())
    print("01" * min(a, b) + "0" * max(0, a - b) + "1" * max(0, b - a))
