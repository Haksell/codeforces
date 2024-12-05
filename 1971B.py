# ruff: noqa: E731, E741
for _ in range(int(input())):
    s = list(input())
    i = next((i for i in range(1, len(s)) if s[i] != s[0]), None)
    if i is None:
        print("NO")
    else:
        print("YES")
        s[0], s[i] = s[i], s[0]
        print("".join(s))
