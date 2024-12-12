# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    print(4 - n if n <= 4 else n & 1)
