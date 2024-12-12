# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input()))
    if n & 1:
        print(1 if any(ai & 1 == 1 for ai in a[::2]) else 2)
    else:
        print(2 if any(ai & 1 == 0 for ai in a[1::2]) else 1)
