# ruff: noqa: E731, E741
from random import shuffle


def ceil_div(numer, denom):
    return -(-numer // denom)


for _ in range(int(input())):
    hc, dc = map(int, input().split())
    hm, dm = map(int, input().split())
    k, w, a = map(int, input().split())
    idxs = list(range(k + 1))
    shuffle(idxs)
    print(
        "YES"
        if any(ceil_div(hc + a * (k - i), dm) >= ceil_div(hm, dc + w * i) for i in idxs)
        else "NO"
    )
