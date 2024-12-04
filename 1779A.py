import re

for _ in range(int(input())):
    n = int(input())
    s = input()
    if len(set(s)) == 1:
        print(-1)
    elif re.fullmatch(r"L+R+", s):
        print(s.index("R"))
    else:
        print(0)
