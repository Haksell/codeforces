# ruff: noqa: E731, E741
import re

for _ in range(int(input())):
    s = input()
    print(2 - bool(re.fullmatch(r"1*0*1*", s)) - all(c == "1" for c in s))
