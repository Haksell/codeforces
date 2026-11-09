from itertools import groupby

for _ in range(int(input())):
    s = input()
    groups = sum(1 for _ in groupby(s))
    print(groups - ("01" in s))
