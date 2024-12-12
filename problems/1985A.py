# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b = input().split()
    print(b[0] + a[1:], a[0] + b[1:])
