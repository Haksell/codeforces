# ruff: noqa: E731, E741
for _ in range(int(input())):
    h, w = map(int, input().split())
    print(min(2, h), min(2, w))
