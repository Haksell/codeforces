# ruff: noqa: E731, E741
for _ in range(int(input())):
    s = input()
    print(s if s[0] == s[-1] else s[:-1] + chr(195 - ord(s[-1])))
