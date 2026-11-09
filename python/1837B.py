from itertools import groupby

for _ in range(int(input())):
    input()
    print(max(sum(1 for _ in v) for _, v in groupby(input())) + 1)
