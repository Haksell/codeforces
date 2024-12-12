from itertools import groupby

for _ in range(int(input())):
    input()
    ans = 0
    for i, (k, v) in enumerate(groupby(input())):
        if i != 0 and k == "P":
            ans = max(ans, sum(1 for _ in v))
    print(ans)