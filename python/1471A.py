# ruff: noqa: E731, E741
def ceil_div(numer, denom):
    return -(-numer // denom)


for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(ceil_div(sum(a), x), sum(ceil_div(y, x) for y in a))
