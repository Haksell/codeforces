# ruff: noqa: E731, E741
for _ in range(int(input())):
    x, y = map(int, input().split())
    q, r = divmod(y, x)
    if r != 0:
        print(0, 0)
    else:
        print(1, q)
