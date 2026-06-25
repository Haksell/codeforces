# ruff: noqa: E731, E741
for _ in range(int(input())):
    l, r = map(int, input().split())
    y = l << 1
    if y <= r:
        print(l, y)
    else:
        print(-1, -1)
