# ruff: noqa: E731, E741
s = input()
i = 0
for c in input():
    if c == s[i]:
        i += 1
print(i + 1)
