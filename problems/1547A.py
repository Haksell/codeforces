# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xf, yf = map(int, input().split())
    res = abs(xa - xb) + abs(ya - yb)
    if (xa == xb == xf and (ya < yf) == (yf < yb)) or (
        ya == yb == yf and (xa < xf) == (xf < xb)
    ):
        res += 2
    print(res)
