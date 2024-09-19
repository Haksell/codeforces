from dataclasses import dataclass
import sys


@dataclass
class Ingredient:
    count: int
    owned: int
    price: int


def solve(money, bacon, sausage, cheese):
    if bacon.count == 0:
        bacon.owned = 0
    if sausage.count == 0:
        sausage.owned = 0
    if cheese.count == 0:
        cheese.owned = 0

    res = min(
        bacon.owned // bacon.count if bacon.count else sys.maxsize,
        sausage.owned // sausage.count if sausage.count else sys.maxsize,
        cheese.owned // cheese.count if cheese.count else sys.maxsize,
    )
    bacon.owned -= res * bacon.count
    sausage.owned -= res * sausage.count
    cheese.owned -= res * cheese.count

    while bacon.owned or sausage.owned or cheese.owned:
        rb = max(0, bacon.count - bacon.owned)
        rs = max(0, sausage.count - sausage.owned)
        rc = max(0, cheese.count - cheese.owned)
        price_required = bacon.price * rb + sausage.price * rs + cheese.price * rc
        if price_required > money:
            return res
        res += 1
        money -= price_required
        bacon.owned += rb - bacon.count
        sausage.owned += rs - sausage.count
        cheese.owned += rc - cheese.count

    price_full = (
        bacon.price * bacon.count
        + sausage.price * sausage.count
        + cheese.price * cheese.count
    )
    return res + money // price_full


def main():
    recipe = input()
    cb, cs, cc = (recipe.count(c) for c in "BSC")
    nb, ns, nc = map(int, input().split())
    pb, ps, pc = map(int, input().split())
    money = int(input())
    bacon = Ingredient(cb, nb, pb)
    sausage = Ingredient(cs, ns, ps)
    cheese = Ingredient(cc, nc, pc)
    print(solve(money, bacon, sausage, cheese))


if __name__ == "__main__":
    main()
