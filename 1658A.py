from itertools import groupby

for _ in range(int(input())):
    n = int(input())
    s = "11" + input().strip("1") + "11"
    ans = 0
    groups = [(k, sum(1 for _ in v)) for k, v in groupby(s)]
    for k, v in groups:
        if k == "1":
            ans += v == 1
        else:
            ans += 2 * (v - 1)
    print(ans)