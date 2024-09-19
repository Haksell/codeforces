import sys


def solve(cb, cs, cc, nb, ns, nc, pb, ps, pc, money):
    if cb == 0:
        nb = 0
    if cs == 0:
        ns = 0
    if cc == 0:
        nc = 0

    res = min(
        nb // cb if cb else sys.maxsize,
        ns // cs if cs else sys.maxsize,
        nc // cc if cc else sys.maxsize,
    )
    nb -= res * cb
    ns -= res * cs
    nc -= res * cc

    while nb or ns or nc:
        rb = max(0, cb - nb)
        rs = max(0, cs - ns)
        rc = max(0, cc - nc)
        price_required = pb * rb + ps * rs + pc * rc
        if price_required > money:
            return res
        res += 1
        money -= price_required
        nb += rb - cb
        ns += rs - cs
        nc += rc - cc

    price_full = pb * cb + ps * cs + pc * cc
    return res + money // price_full


def main():
    recipe = input()
    cb, cs, cc = (recipe.count(c) for c in "BSC")
    nb, ns, nc = map(int, input().split())
    pb, ps, pc = map(int, input().split())
    money = int(input())
    print(solve(cb, cs, cc, nb, ns, nc, pb, ps, pc, money))


if __name__ == "__main__":
    main()
