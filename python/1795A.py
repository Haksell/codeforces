from itertools import groupby

for _ in range(int(input())):
    input()
    s = input() + input()[::-1]
    print(
        "YES"
        if sum(max(0, sum(1 for _ in v) - 1) for _, v in groupby(s)) <= 1
        else "NO"
    )
