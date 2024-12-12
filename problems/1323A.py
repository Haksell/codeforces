# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ie = next((i for i, ai in enumerate(a, 1) if ai & 1 == 0), None)
    if ie is not None:
        print(1)
        print(ie)
    elif n >= 2:
        print(2)
        print(1, 2)
    else:
        print(-1)
