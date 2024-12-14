# ruff: noqa: E731, E741
def friends(n):
    return n * (n - 1) >> 1


def get_mini(players, teams):
    small = players // teams
    big = small + 1
    big_count = players % teams
    small_count = teams - big_count
    return small_count * friends(small) + big_count * friends(big)


def get_maxi(players, teams):
    return friends(players - teams + 1)


players, teams = map(int, input().split())
print(get_mini(players, teams), get_maxi(players, teams))
