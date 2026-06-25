# ruff: noqa: E731, E741
for _ in range(int(input())):
    x, y, a, b = map(int, input().split())
    d = y - x
    q, r = divmod(y - x, a + b)
    print(-1 if r else q)
