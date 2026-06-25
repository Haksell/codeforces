# ruff: noqa: E731, E741
for _ in range(int(input())):
    h, w, x, y = map(int, input().split())
    burles = 0
    for _ in range(h):
        row = input()
        t = row.count("..")
        o = row.count(".")
        burles += t * y + (o - 2 * t) * x if y < 2 * x else o * x
    print(burles)
