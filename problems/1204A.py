# ruff: noqa: E731, E741
s = input()
n = len(s) - all(c == "0" for c in s[1:])
print(n + 1 >> 1)
