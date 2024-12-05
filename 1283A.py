# ruff: noqa: E731, E741
for _ in range(int(input())):
    h, m = map(int, input().split())
    print(1440 - 60 * h - m)
