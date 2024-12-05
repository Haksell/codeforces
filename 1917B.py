# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    s = input()
    chars = set()
    res = 0
    for c in s:
        chars.add(c)
        res += len(chars)
    print(res)
