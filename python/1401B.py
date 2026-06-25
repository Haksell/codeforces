# ruff: noqa: E731, E741
for _ in range(int(input())):
    x1, _, z1 = map(int, input().split())
    _, y2, z2 = map(int, input().split())
    a = min(z1, y2)
    print((a - z2 + min(x1 + z1 - a, z2)) << 1)
