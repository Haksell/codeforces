# ruff: noqa: E731, E741
n = int(input())
s = input()
i = 0
inc = 0
res = []
while i < n:
    res.append(s[i])
    inc += 1
    i += inc
print("".join(res))
