# ruff: noqa: E731, E741
def ceil_div(numer, denom):
    return -(-numer // denom)


cups = sum(map(int, input().split()))
medals = sum(map(int, input().split()))
shelves_needed = ceil_div(cups, 5) + ceil_div(medals, 10)
print("YES" if int(input()) >= shelves_needed else "NO")
