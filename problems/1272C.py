from itertools import groupby

input()
s = input()
chars = set(input().split())
groups = [sum(1 for _ in v) for k, v in groupby(s, key=chars.__contains__) if k]
print(sum(n * (n + 1) >> 1 for n in groups))