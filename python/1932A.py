# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    s = input()
    res = i = 0
    while i < len(s):
        res += s[i] == "@"
        if i + 1 < n and s[i + 1] in ".@":
            i += 1
        elif i + 2 < n and s[i + 2] in ".@":
            i += 2
        else:
            break
    print(res)
