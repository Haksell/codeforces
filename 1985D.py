# ruff: noqa: E731, E741
for _ in range(int(input())):
    h, w = map(int, input().split())
    x = y0 = y1 = None
    for y in range(h):
        s = input()
        xs = [x for x in range(w) if s[x] == "#"]
        if len(xs) == 1:
            if y0 is None:
                y0 = y
                x = xs[0]
            else:
                y1 = y
    print((y0 if y1 is None else y0 + y1 >> 1) + 1, x + 1)
