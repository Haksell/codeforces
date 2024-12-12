# ruff: noqa: E731, E741
def ceil_div(numer, denom):
    return -(-numer // denom)


for _ in range(int(input())):
    cards, jokers, players = map(int, input().split())
    hand = cards // players
    print(jokers if jokers <= hand else hand - ceil_div(jokers - hand, players - 1))
