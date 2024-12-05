# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    s = input()
    t = input()
    diff = [i for i in range(n) if s[i] != t[i]]
    if len(diff) == 0:
        print("Yes")
    elif len(diff) != 2:
        print("No")
    else:
        i, j = diff
        print("Yes" if s[i] == s[j] and t[i] == t[j] else "No")
