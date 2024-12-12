# ruff: noqa: E731, E741
last = res = 0
for c in input():
    loc = ord(c) - 97
    res += min(abs(loc - last), 26 + loc - last, 26 + last - loc)
    last = loc
print(res)
