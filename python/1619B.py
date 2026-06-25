# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input()) + 0.5
    print(int(n ** (1 / 2)) + int(n ** (1 / 3)) - int(n ** (1 / 6)))
