# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        print(0, 0)
    else:
        e = abs(a - b)
        print(e, min(a % e, -a % e))
