# ruff: noqa: E731, E741
def ceil_div(numer, denom):
    return -(-numer // denom)


for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if b >= a:
        print(b)
    elif d >= c:
        print(-1)
    else:
        snoozes = ceil_div(a - b, c - d)
        print(b + snoozes * c)
