# ruff: noqa: E731, E741
def ceil_div(numer, denom):
    return -(-numer // denom)


for _ in range(int(input())):
    x, y, k = map(int, input().split())
    t = k * (y + 1)
    print(k + ceil_div(t - 1, x - 1))
