# ruff: noqa: E731, E741
import re

for _ in range(int(input())):
    ab = input()
    m = re.fullmatch(r"([1-9]0*)([1-9]\d*)", ab)
    if not m:
        print(-1)
        continue
    a, b = map(int, m.groups())
    if a >= b:
        print(-1)
    else:
        print(a, b)
