# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(0 if 0 == a == b == c == d else 2 if 1 == a == b == c == d else 1)
