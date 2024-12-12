# ruff: noqa: E731, E741
for _ in range(int(input())):
    s = input()
    print("NO" if len(s) & 1 or s[0] == ")" or s[-1] == "(" else "YES")
