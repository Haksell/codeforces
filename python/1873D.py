# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    res = i = 0
    while i < n:
        if s[i] == "B":
            res += 1
            i += k
        else:
            i += 1
    print(res)
