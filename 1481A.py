from collections import Counter


for _ in range(int(input())):
    x, y = map(int, input().split())
    s = input()
    c = Counter(s)
    if -c["L"] <= x <= c["R"] and -c["D"] <= y <= c["U"]:
        print("YES")
    else:
        print("NO")
