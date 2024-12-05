# ruff: noqa: E731, E741


def ceil_div(numer, denom):
    return -(-numer // denom)


n, m, a = map(int, input().split())
print(ceil_div(n, a) * ceil_div(m, a))
