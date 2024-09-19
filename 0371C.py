from dataclasses import dataclass
import sys


@dataclass
class Ingredient:
    count: int
    owned: int
    price: int


def solve(money, ingredients):
    res = min(i.owned // i.count if i.count else sys.maxsize for i in ingredients)
    for i in ingredients:
        i.owned -= res * i.count

    while any(i.owned and i.count for i in ingredients):
        required = [max(0, i.count - i.owned) for i in ingredients]
        price_required = sum(i.price * r for i, r in zip(ingredients, required))
        if price_required > money:
            return res
        res += 1
        money -= price_required
        for i, r in zip(ingredients, required):
            i.owned += r - i.count

    price_full = sum(i.price * i.count for i in ingredients)
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
    print(solve(money, [bacon, sausage, cheese]))


if __name__ == "__main__":
    main()
