from collections import defaultdict


def get_first(lines, winners, max_score):
    d = defaultdict(int)
    for player, n in lines:
        if player in winners:
            d[player] += n
            if d[player] >= max_score:
                return player


d = defaultdict(int)
lines = [input().split() for _ in range(int(input()))]
lines = [(player, int(n)) for player, n in lines]
for player, n in lines:
    d[player] += n
max_score = max(d.values())
winners = {k for k, v in d.items() if v == max_score}
print(get_first(lines, winners, max_score))
